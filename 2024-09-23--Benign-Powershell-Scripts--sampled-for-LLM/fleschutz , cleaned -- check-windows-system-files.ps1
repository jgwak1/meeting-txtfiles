#Requires -RunAsAdministrator

try {
	sfc /verifyOnly
	if ($lastExitCode -ne "0") { throw "'sfc /verifyOnly' failed" }

	"✔️ checked Windows system files"
	exit 0
} catch {
	"⚠️ Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0])"
	exit 1
}
