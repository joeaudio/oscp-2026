# 03 — Web mapping, sessions and client side

**Outcome:** map an app's trust boundaries before testing a payload. In the
local lab, start `python3 labs/miniweb.py` and use `BASE=http://127.0.0.1:8765`.

## Tutorial

An HTTP request has method, path, headers and body. The server may trust
cookies or hidden form fields it should validate. Compare responses with and
without a cookie, and record status, length and key headers:

```sh
curl -i "$BASE/"
curl -i "$BASE/robots.txt"
curl -i "$BASE/admin"
curl -i -H 'Cookie: role=admin' "$BASE/admin"
```

The local app intentionally trusts a client-controlled role cookie. A 200
response after changing it demonstrates a broken access check in this toy
app; it does not prove arbitrary code execution. In a real app, test only
authorized accounts and objects. Inspect links, JavaScript, forms, API paths,
redirects, response codes, and session changes. Burp Free Repeater is useful
for changing one request field at a time; record the exact before/after.

For cross-site scripting, distinguish **reflected** input (returned in the
same response), **stored** input (persisted for later readers), and **DOM**
execution (client-side script inserts untrusted data). The important question
is whether untrusted text reaches an executable browser context. Start with
an inert marker such as `OSCPTEST123`; inspect encoded output before any
script payload. This repo contains no browser victim service.

Client-side attacks depend on a user action and a target application version.
Do not send files or links to real users. For study, compare a harmless
document's metadata and its intended open path in your own VM; state what
would have to happen for code execution. Treat Office macro and shortcut
topics as authorized-lab techniques, not default engagement steps.

## Challenge

Map every local miniweb endpoint without reading its source first. Identify
one trust boundary failure and one response that is correctly denied.

<details><summary>Hint 1</summary>`robots.txt` and HTML links are part of the attack surface, but neither guarantees an exploitable path.</details>
<details><summary>Hint 2</summary>Change only the `role` cookie and compare `/admin` responses.</details>
<details><summary>Check</summary>The role cookie grants access in this local toy service. The report should state exact requests and responses, impact limited to the lab, and a fix: enforce roles in a server-side authenticated session.</details>
