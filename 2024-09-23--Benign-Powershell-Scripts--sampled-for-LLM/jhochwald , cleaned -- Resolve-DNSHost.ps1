function Resolve-DNSHost
{
   [CmdletBinding(ConfirmImpact = 'None')]
   [OutputType([psobject])]
   param
   (
      [Parameter(Mandatory,
         ValueFromPipeline,
         ValueFromPipelineByPropertyName,
         Position = 0,
         HelpMessage = 'Hostname (Single, or multiple) to test.')]
      [ValidateNotNullOrEmpty()]
      [String[]]
      $HostEntry
   )

   begin
   {
      $Obj = @()
      $Object = @()
   }

   process
   {
      $HostEntry | ForEach-Object -Process {
         $Obj += New-Object -TypeName psobject -Property @{
            HostName  = $_
            IPAddress = $([Net.Dns]::gethostentry($_).AddressList.IPAddressToString)
         }
      }
      $Object = ($Obj | Select-Object -Property Hostname, IPAddress)
   }
   end
   {
      $Object
   }
}
