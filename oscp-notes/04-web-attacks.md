# 04 — Traversal, file inclusion, upload and command injection

**Outcome:** explain the input-to-sink path, not just a payload. Start the
local miniweb for the bounded traversal exercise.

## Directory traversal and inclusion

`/files?name=readme.txt` is meant to read a file under `public/`. The toy
service resolves a name under `public/` but allows a `..` step into its
own `data/hidden/` area. It deliberately refuses paths outside `data/`.

```sh
curl -i 'http://127.0.0.1:8765/files?name=readme.txt'
curl -i 'http://127.0.0.1:8765/files?name=../hidden/ops.txt'
```

Compare both responses and state the expected boundary. Directory traversal
reads a file outside the intended directory. File inclusion means the app
includes a file in execution/rendering; the two may overlap but are not the
same. Encodings may alter the path a server sees, so decode and normalize
before deciding whether a file is allowed.

## Upload and command injection

An upload test asks where a file is stored, how its extension and content are
validated, and whether the server executes it. An allowed upload is not by
itself code execution. Try only a harmless text marker in an authorized lab.

Command injection occurs when input becomes part of a shell command. Compare:

```python
# Risky design: a shell interprets user-controlled metacharacters.
subprocess.run("ping -c 1 " + host, shell=True)
# Safer design: argument vector; validate host and cap time/output too.
subprocess.run(["ping", "-c", "1", host], shell=False, timeout=3)
```

Do not run the risky example on this workstation. In a real assessment,
start with a harmless time or marker check inside scope and verify the
observed effect. The local lab does not expose an OS-command sink.

## Challenge

Demonstrate the local traversal, then write the one-line path validation
rule that would prevent leaving `public/`. For upload and injection, draw
the trust boundary and propose a non-destructive test for an authorized lab.

<details><summary>Hint 1</summary>The vulnerable path joins `public/` and a user-supplied name before resolving it.</details>
<details><summary>Hint 2</summary>The final resolved path should be a child of the allowed directory, not merely the broader data root.</details>
<details><summary>Check</summary>The traversal reads synthetic `hidden/ops.txt`. A correct fix compares the resolved path with the resolved `public/` root. For command execution, argument arrays and input validation remove shell interpretation; timeout limits damage but does not fix a shell sink.</details>
