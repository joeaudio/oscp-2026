# 09 — Windows privilege escalation

**Outcome:** identify a privilege boundary in services, scheduled tasks or
token rights, then verify the exact condition in an authorized Windows lab.

## Tutorial

Start with identity and groups, then enumerate services and tasks:

```powershell
whoami /all
systeminfo
Get-CimInstance Win32_Service | Select-Object Name,StartName,PathName,State
schtasks /query /fo LIST /v
```

For a suspicious service, inspect its configuration and file permissions:

```cmd
sc qc DemoService
icacls "C:\Program Files\Demo App\service.exe"
```

A writable service binary matters only if a privileged service uses it and
you can trigger or wait for restart. Unquoted service paths matter only when
the path contains spaces, a candidate executable location is writable, and
the service's execution context is privileged. Do not infer exploitability
from a scanner label alone. Scheduled tasks similarly need both a privileged
run context and a writable action path or arguments.

Token privileges such as `SeImpersonatePrivilege` can enable certain paths,
but presence is not itself a working exploit. Verify OS version, service
context, and a reviewed technique in a disposable lab. Keep original binary
hashes/backups and document restoration steps.

## Challenge

Use `fixtures/windows.txt`. Rank its service and task findings. State what
`icacls` result would make each exploitable and what result would reject it.
In a Windows lab, record `whoami /all` and one service's start account/path.

<details><summary>Hint 1</summary>Look for both privilege of the runner and control of an executable or argument.</details>
<details><summary>Hint 2</summary>A non-admin service running from a writable path is not a privilege-escalation path by itself.</details>
<details><summary>Check</summary>The fixture makes the scheduled task script the first hypothesis, pending ACL verification. The service path requires its own file/directory ACL and restart check. Report only verified execution context.</details>
