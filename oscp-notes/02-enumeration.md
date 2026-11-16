# 02 — Host and service enumeration

**Outcome:** produce a service map, then choose a service-specific test. Scan
only named authorized addresses. `TARGET` below is a placeholder, not a
default target.

## Tutorial

TCP and UDP are different transports. A closed TCP port answers differently
from a filtered one; UDP silence does not prove a service absent. Start with a
bounded TCP scan, then inspect the discovered ports:

```sh
TARGET=192.0.2.10
nmap -sT -Pn -p- --min-rate 100 -oN tcp-all.txt "$TARGET"
nmap -sV -sC -Pn -p 22,80,445 -oN tcp-detail.txt "$TARGET"
```

`-sT` uses a full TCP connect, `-Pn` skips host discovery, `-p-` covers all
TCP ports, and `-oN` saves evidence. Replace `22,80,445` with ports actually
found. Avoid high-rate scans on fragile labs. `-sC` runs default NSE scripts;
read the script category and scope before using additional scripts.

Service follow-ups, each only when present and in scope:

```sh
dig @192.0.2.10 example.test ANY       # DNS response, not proof of zone transfer
curl -i http://192.0.2.10/             # headers, redirect and body
smbclient -L //192.0.2.10 -N           # anonymous SMB share listing attempt
nc -nv 192.0.2.10 25                   # SMTP banner; quit after observation
```

For DNS, a failed `ANY` response says little; request A, MX, TXT and NS
records with an authorized domain. For SMB, `NT_STATUS_ACCESS_DENIED` is a
result, not a reason to claim shares exist. For HTTP, follow redirects and
inspect virtual hosts when evidence points there. Save every output under an
ignored target folder.

## Challenge

From `fixtures/scan.txt`, pick the first two service checks and explain what
each possible result would mean. Then, on a named lab host, do a 30-minute
enumeration without a broad vulnerability scanner.

<details><summary>Hint 1</summary>List open ports and exact banners. Do not infer software version from a port number alone.</details>
<details><summary>Hint 2</summary>HTTP: request root and headers. SMB: list shares without credentials only if allowed.</details>
<details><summary>Check</summary>Deliver a table with port, observed service, exact evidence file, next test, and a confidence note. At least one hypothesis should be rejected or marked unconfirmed.</details>
