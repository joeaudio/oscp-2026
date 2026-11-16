# 08 — Linux privilege escalation

**Outcome:** build a ranked hypothesis from permissions and processes before
running a helper script. Execute only on a lab machine where you have shell
access and permission to test escalation.

## Tutorial

Record your current identity and host first:

```sh
id; hostname; uname -a
sudo -l
ss -tulpn
find / -perm -4000 -type f 2>/dev/null
getcap -r / 2>/dev/null
```

`sudo -l` tells you exact delegated commands and whether a password is needed.
SUID programs run with the owner's effective identity; a SUID bit alone is
not a vulnerability. Linux capabilities grant specific powers, so read the
capability and executable together. Check writable scripts run by root,
cron/timers, service units, PATH resolution, and file ownership. Avoid
executing a broad enumeration script before you know what it collects.

Worked interpretation: a root cron job invokes `/opt/backup/run.sh` every
minute, and your user can edit that script. The hypothesis is that a script
change would execute as root. Verify owner, mode, scheduler and exact command
in the authorized lab before any modification. The report should show the
permission boundary and restore the original file if the lab permits.

Kernel exploits have host-wide crash risk. Treat the exact kernel/build and
patch state as preconditions and prefer a configuration path when one exists.

## Challenge

Read `fixtures/linux.txt`. Identify the strongest escalation hypothesis, two
checks that would confirm it, and one observation that would disprove it.
Then perform manual enumeration on an authorized Linux VM without using
LinPEAS for the first 20 minutes.

<details><summary>Hint 1</summary>Focus on a scheduled root action and a file writable by the low-privilege user.</details>
<details><summary>Hint 2</summary>Check the scheduler target and the script's owner/mode, not only its filename.</details>
<details><summary>Check</summary>The synthetic job plus writable script is a strong hypothesis, not yet proof of root execution. A safe lab check records `systemctl cat` or crontab, `stat`, and a controlled marker before claiming impact.</details>
