# Local synthetic web lab

Needs only Python 3. It binds to loopback, uses invented data, stores nothing,
and has no connection to OffSec infrastructure. Do not change the bind address
or expose it to another network; the app is intentionally vulnerable.

```sh
python3 -m unittest discover -s labs -p 'test_*.py'
python3 labs/miniweb.py
# in another terminal:
curl -i http://127.0.0.1:8765/
```

Complete these without opening the source first:

1. Map endpoints from HTML and `robots.txt`. Record status/length for each.
2. Find a client-controlled value that changes `/admin` from 403 to 200.
3. Read the synthetic private file through `/files` without an absolute path.
4. Prove that one search input returns all three documents and a paired input
   returns none. Explain why this is more convincing than a single SQL error.
5. Inspect `miniweb.py`. Point to the exact trust-boundary mistake for each
   finding and describe a server-side fix.

Use the target template and write one finding in `lab-report/template.md`.
Lessons [03](../oscp-notes/03-web-method.md),
[04](../oscp-notes/04-web-attacks.md), and
[05](../oscp-notes/05-sqli.md) have staged hints and checks. Stop the lab with
Ctrl-C. It does not provide a full OSCP host or AD environment.
