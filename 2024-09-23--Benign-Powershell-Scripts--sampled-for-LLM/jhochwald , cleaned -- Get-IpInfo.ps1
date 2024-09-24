[CmdletBinding(ConfirmImpact = 'None')]
[OutputType([psobject])]
param ()

begin
{
   $IpAddressInfo = $null
}
process
{
   $IpAddressInfo = @(
      (([Net.DNS]::GetHostAddresses([Net.Dns]::GetHostByName(($env:COMPUTERNAME)).HostName) | Where-Object -FilterScript {
            $PSItem.IsIPv6LinkLocal -eq $false
         }).IPAddressToString | Where-Object -FilterScript {
         $_ -ne '::1'
      })
   )
}
end
{
   $IpAddressInfo
   $IpAddressInfo = $null
}
