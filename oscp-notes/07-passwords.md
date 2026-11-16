# 07 — Authentication and password attacks

**Outcome:** choose an authentication test based on protocol and authorization,
then distinguish online guessing from offline hash work.

## Tutorial

Online guessing sends attempts to a service and can lock accounts. Confirm
scope, rate limits, account policy and whether the credential was supplied.
Start by validating one known credential, not spraying a list. Offline
cracking operates on a hash obtained lawfully in the lab and does not contact
the target service, but the hash may still be sensitive: keep it outside Git.

For a harmless local exercise, create a toy SHA-256 value and a tiny wordlist:

```sh
printf 'labonly123' | sha256sum
printf 'welcome\nlabonly123\npassword\n' > /tmp/oscp-toy-words.txt
```

Explain why a fast unsalted digest is easy to test offline. Do not confuse
that toy digest with an NTLM, Net-NTLMv2, Kerberos ticket or password-manager
key file; each has different capture context and cracking format. `john
--list=formats` or `hashcat --help` identifies local supported formats;
use a known test hash and verify the tool's mode before a lab attempt.

For a network login, note protocol, realm/domain, username format, source IP,
and lockout behavior. Passing an NTLM hash authenticates to some services
without recovering plaintext; it is not the same as cracking the hash.
Net-NTLMv2 is a challenge-response exchange, not the stored NTLM hash.
Relaying authentication involves other conditions and may be prohibited by
scope or exam spoofing rules; check the current policy.

## Challenge

Classify these observations: (A) a local SHA-256 digest, (B) an HTTP login
form, (C) a captured Net-NTLMv2 response, (D) an NTLM hash from an authorized
lab account. For each, choose a non-destructive first check and say whether
the target service receives attempts.

<details><summary>Hint 1</summary>Split offline artifacts from online authentication interfaces.</details>
<details><summary>Hint 2</summary>A response to a challenge cannot be used interchangeably with the stored NTLM hash.</details>
<details><summary>Check</summary>A and C are offline analysis candidates if lawfully obtained; B is online and needs rate/lockout controls; D can be tested offline or in a narrowly authorized pass-the-hash lab. Never place any real artifact in this repo.</details>
