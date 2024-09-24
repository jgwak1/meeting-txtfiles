[CmdletBinding(SupportsShouldProcess = $true)]

param(
    [int] $MaxConnections = 2
)

Begin
{
    $script:termsrv = 'C:\Windows\System32\termsrv.dll'

    function PatchTermsrv
    {
        Write-Host 'reading termsrv.dll'
        if ($PSVersionTable.PSEdition.IndexOf('Core') -ge 0)
        {
            $bytes = Get-Content $termsrv -Raw -asByteStream
        }
        else
        {
            $bytes = Get-Content $termsrv -Raw -Encoding Byte
        }

        Write-Host 'converting to byte array; one moment please'
        $text = $bytes.forEach('ToString', 'X2') -join ' '

        Write-Host 'paching termsrv.dll'
        
        $pattern = ([regex]'39 81 3C 06 00 00(\s\S\S){6}')
        $patch = 'B8 00 01 00 00 89 81 38 06 00 00 90'
        $match = Select-String -Pattern $pattern -InputObject $text
        if ($match -ne $null)
        {
            $text = $text -replace $pattern, $patch
        }
        elseif (Select-String -Pattern $patch -InputObject $text)
        {
            Write-Output '*** termsrv.dll is already patched'
            return $false
        }
        else
        { 
            Write-Output '*** pattern not found'
            return $false
        }

        [byte[]] $bytes = -split $text -replace '^', '0x'

        Set-Content $env:TEMP\termsrv.dll.patched -Force -Encoding Byte -Value $bytes

        Write-Host 'validating patch'

        fc.exe /b $env:TEMP\termsrv.dll.patched $termsrv | Out-File $env:TEMP\termsrv.txt
        if ($LASTEXITCODE -eq 0)
        {
            Write-Host 'termsrv.dll was not patched'
            return $false
        }

        return (Get-Content $env:TEMP\termsrv.txt).Count -eq 12
    }

    function StopServices
    {
        Write-Host 'stopping services'
        Stop-Service UmRdpService -Force

        sc.exe config TermService start= disabled
        $svcid = Get-CimInstance -Class Win32_Service -Filter "Name LIKE 'TermService'" | Select -ExpandProperty ProcessId
        taskkill /f /pid $svcid
    }

    function TakeOwnership
    {
        $script:savedAcl = Get-Acl $termsrv
        Write-Host "termsrv.dll owner: $($savedAcl.owner))"

        Write-Host 'creating termsrv backup'
        Copy-Item $termsrv "$termsrv.backup" -Force

        Write-Host 'taking ownership and granting full access'
        takeown /f $termsrv
        $owner = (Get-Acl $termsrv).Owner

        cmd /c "icacls $termsrv /Grant $($owner):F /C"
    }


    function RestoreOwnership
    {
        Write-Host 'restoring ownership'
        Set-Acl $termsrv $savedAcl
    }

    function StartServices
    {
        Write-Host 'starting services'
        sc.exe config TermService start= demand
        Start-Service TermService
        Start-Service UmRdpService
    }

    function SetGlobalPolicy
    {
        Write-Host 'setting Global Policy'

        $0 = 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services'

        Set-ItemProperty $0 -Name 'MaxInstanceCount' -Type DWord -Value $MaxConnections

        Set-ItemProperty $0 -Name 'fSingleSessionPerUser' -Type DWord -Value 0
    }

    function EnableRemoteConnections
    {
        Write-Verbose 'enabling Remote Desktop w/o Network Level Authentication...'

        $0 = 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server'
        Set-ItemProperty $0 -Name 'fDenyTSConnections' -Type DWord -Value 0
        Set-ItemProperty "$0\WinStations\RDP-Tcp" -Name 'UserAuthentication' -Type DWord -Value 0
        Enable-NetFirewallRule -Name 'RemoteDesktop*'
    }
}
Process
{

    if (PatchTermsrv)
    {

        Write-Host 'applying patch'

        StopServices
        TakeOwnership

        Write-Host 'ovewriting termsrv.dll'
        Copy-Item $env:TEMP\termsrv.dll.patched $termsrv -Force

        RestoreOwnership
        StartServices

        SetGlobalPolicy
        EnableRemoteConnections
    }
}
