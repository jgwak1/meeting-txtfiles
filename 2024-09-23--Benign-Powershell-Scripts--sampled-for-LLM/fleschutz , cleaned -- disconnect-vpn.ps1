try {
	$Connections = (Get-VPNConnection)
	foreach($Connection in $Connections) {
		if ($Connection.ConnectionStatus -ne "Connected") { continue }
		"Disconnecting $($Connection.Name)..."
		& rasdial.exe "$($Connection.Name)" /DISCONNECT
		if ($lastExitCode -ne "0") { throw "Disconnect failed with exit code $lastExitCode" }
		"Disconnected now."
		exit 0
	}
	throw "No VPN connection found."
} catch {
	"⚠️ Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0])"
	exit 1
}
