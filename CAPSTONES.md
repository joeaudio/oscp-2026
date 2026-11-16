# Timed capstones

Do these without opening the lesson checks until the timer ends. Put real
outputs under ignored `oscp-work/targets/`, and submit only your own summary
for review. Synthetic fixtures are deliberately incomplete: a good answer
can say **not yet proven**.

## A — Local web assessment (60 minutes)

Start `python3 labs/miniweb.py` without reading its source. In 40 minutes,
map reachable paths, prove one access-control issue, one file boundary issue,
and one injection issue with paired requests. Spend the remaining 20 minutes
writing one finding with exact request/response, impact limited to the toy
app, a concrete fix, and a retest. Test the fixes by reading the code only
after writing your own hypotheses.

**Pass check:** all three claims have reproducible requests; no claim of OS
shell or real credential compromise; server-side fixes address the actual
trust boundaries. Lessons 03–05 contain staged hints.

## B — Service to foothold decision (45 minutes)

Read only `fixtures/scan.txt`. Build a service table and a 30-minute manual
test order. For each service, write one likely lead and one disconfirming
result. Choose a public exploit only after writing its required version,
configuration and reachability conditions. Do not invent a successful shell.

**Pass check:** the plan distinguishes banner from proof, avoids unscoped
automation, and cites exact fixture lines. Lessons 01, 02, 06 and 13 help.

## C — Post-access triage (60 minutes)

Treat `fixtures/linux.txt` and `fixtures/windows.txt` as two different
authorized lab hosts. For each, rank two privilege-escalation hypotheses,
specify the least disruptive confirmation, and state a possible false
positive. Write the two report paragraphs you would use if the checks
confirmed the issue, with placeholders rather than invented screenshots.

**Pass check:** Linux scheduled execution and Windows task/service contexts
are discussed with ACL verification; no escalation is claimed from a
filename alone. Lessons 08 and 09 help.

## D — AD path and pivot (90 minutes)

Read `fixtures/ad-paths.csv`. Draw every verified edge and every unverified
edge in different styles. Starting as `student`, identify the nearest
reachable host, a possible credential lead, and what must be confirmed before
claiming control of `DC1`. Add a loopback-bound SSH forwarding diagram for
one in-scope internal HTTP service. Finish with a private credential map
containing labels only, no actual secrets.

**Pass check:** no network reachability edge is mistaken for admin rights;
each credential use has a source and permitted scope; the tunnel diagram
shows both connections and listener binding. Lessons 10 and 11 help.

## E — Mock report review (45 minutes)

Take your own A–D notes. Mark each assertion as **observed**, **inferred**,
or **unverified**. Remove unsupported impact claims. Check command order,
target identity, evidence paths, remediation and cleanup. Reproduce one
finding from a clean local-lab restart. Grade your own work using
[ASSESSMENT.md](ASSESSMENT.md); gaps stay gaps until an unaided repeat.

This pack cannot substitute for full Linux, Windows and AD targets. Use your
own authorized labs for those practical days and keep their data private.
