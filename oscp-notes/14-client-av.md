# 14 — Client-side paths and antivirus boundaries

**Outcome:** explain the user action and defensive control needed for a
client-side path, and distinguish a detected file from blocked execution.

## Tutorial

A client-side attack starts when a user opens or processes attacker-controlled
content. The chain is: delivery → user/application action → vulnerable
parser/feature → execution → access. Every link needs evidence. Office macros,
shortcuts and library files are course topics; do not send a payload to a
real person. Use a disposable VM and a harmless marker file when practicing.

Antivirus/EDR can inspect files, memory, scripts and behavior. A hash/name
match is different from behavior detection. If a test file is quarantined,
record *which* control acted and at what point. Do not claim “AV bypass”
because one test was not detected. The practical skill is to adapt and
validate a narrow technique in an authorized lab while retaining a clear
report trail; this public guide includes no weaponized document or bypass
binary.

Worked reasoning example:

```text
Observation: a lab document is downloaded but never opened.
Conclusion: delivery worked; execution has not been demonstrated.
Next check: in a disposable VM, open a harmless test document and observe
the application warning, macro policy and process tree.
```

## Challenge

Write the five-link chain for a fictional shortcut file and mark which
links are established by “HTTP 200 download” alone. Propose a safe local
test that distinguishes file detection from execution blocking.

<details><summary>Hint 1</summary>A download confirms delivery, not user action or code execution.</details>
<details><summary>Hint 2</summary>Observe both security-product event and process creation in a disposable lab.</details>
<details><summary>Check</summary>Only delivery is established. A sound test uses a benign marker, a controlled VM, and explicit evidence for open/execute/block decisions.</details>
