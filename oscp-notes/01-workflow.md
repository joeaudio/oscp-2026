# 01 — Workflow, scope and evidence

**Outcome:** turn observations into a repeatable attack path and a readable
finding. Start with a written scope: allowed IPs, dates, credentials, and
whether destructive tests are allowed. A command is evidence only when its
target, time, output and interpretation are recorded. Never run examples
against a third-party host without authorization.

## Method

1. **Orient:** identify the target and what access you already have.
2. **Enumerate:** collect facts with low-impact probes; distinguish facts from
   hypotheses.
3. **Prioritize:** pick the most plausible path and state what would falsify it.
4. **Test:** make one controlled change, record exact command and result.
5. **Reproduce:** repeat the finding from a clean state, then write impact and
   a concrete fix. Keep raw output and screenshots outside the public repo.

Example target note (fictional):

```text
Host: 192.0.2.10 (documentation address; replace only in your authorized lab)
Fact: TCP 80 returns HTTP 200 and Server: nginx.
Hypothesis: an exposed application route might reveal an admin function.
Next check: map links and robots.txt; compare status and response length.
Result: /admin returns 403, so no access claim yet.
```

Record why a tool was used. `nmap -sV` probes service versions; its banner is
an observation, not proof of a vulnerability. `curl -i` shows HTTP headers;
`-i` does not make the application safe or vulnerable.

## Attempt before hints

Use `fixtures/scan.txt`. Write three facts, two hypotheses, and the next
low-impact check for each hypothesis. Put it in a copy of
`oscp-work/host-template-dir/target.md` under ignored `oscp-work/targets/`.

<details><summary>Hint 1</summary>Separate what the output literally says from what a version number might imply.</details>
<details><summary>Hint 2</summary>Look at HTTP, SMB and SSH separately; ask what each service exposes without credentials.</details>
<details><summary>Check</summary>The fixture proves ports and banners only. It does not prove anonymous SMB access, a vulnerable web app, or valid SSH credentials. A good next check is a targeted HTTP request or SMB share listing on an authorized host, with exact results recorded.</details>

## Report habit

After each session, write: starting state → exact action → evidence → result
→ impact → fix. A screenshot without the command/context is weak evidence.
Before a real exam, use the live OffSec guide for proof and report rules.
