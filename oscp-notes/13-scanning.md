# 13 — Vulnerability scanning and validation

**Outcome:** use scan output as a lead, not a verdict. In preparation labs,
know what a scanner sends and why it may be wrong. The live exam guide
prohibits mass vulnerability scanners such as Nessus and OpenVAS on OSCP+.

## Tutorial

An unauthenticated scanner sees network behavior; an authenticated one may
see packages/configuration, but only with supplied credentials and permission.
Neither replaces manual validation. Nmap's scripting engine can make a
targeted check; read script behavior before use:

```sh
nmap --script-help http-title
nmap -sT -Pn -p 80 --script http-title 192.0.2.10
```

The documentation address is a placeholder. `http-title` reports a page
title, not a vulnerability. A version-to-CVE match needs exact product,
feature and patch state, plus a non-destructive behavioral check. Track
scanner confidence separately from your own evidence. A false positive
may come from a backported patch; a false negative may come from an unusual
port or disabled banner.

## Challenge

A report says “nginx 1.22.1 is vulnerable” based only on `fixtures/scan.txt`.
Rewrite it as a hypothesis and list three checks before assigning impact.
In an authorized lab, use one NSE information script and record exactly
what it did and did not establish.

<details><summary>Hint 1</summary>Look for build/patch state and the specific vulnerable feature, not only a banner.</details>
<details><summary>Hint 2</summary>Compare a known-safe request with a targeted behavior check and observe a changed response.</details>
<details><summary>Check</summary>The fixture establishes only an observed banner. It contains no evidence of a specific vulnerability or impact. The rewrite should avoid a definitive claim until validated.</details>
