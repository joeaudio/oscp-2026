# Current study state

Updated 17 November 2026 (Australia/Sydney).

- Public study pack drafted for delivery by 19 December 2026: 15 original
  lessons, timed capstones, dated plan, synthetic fixtures, loopback web lab, report/target
  templates, setup instructions and a staged-file guard.
- The supplied `oscp-master.zip` was inspected for folder structure only.
  No third-party course, VPN, auth, target or report content was copied.
- Local lab and guard checks were run during preparation; see Git history
  and rerun `python3 -m unittest discover -s labs -p 'test_*.py'` plus the
  equivalent command for `tools/` after cloning.
- Learner's actual target performance is **not demonstrated**. Do not infer
  exam readiness from this pack or from a passing local unit test.
- Local Git history exists and `origin` points to `joeaudio/oscp-2026`.
  The unauthenticated upload attempt returned “Repository not found”; GitHub
  CLI has no login, and the available SSH key is not authorized by GitHub.
  Publication is pending account authentication and destination access.

## Next learner action

Without looking at a hint, read `fixtures/scan.txt` and write three facts,
two hypotheses and one disconfirming check for each in a private target note.
Record the result, gap and next review in ignored `private/daily-log.md`.
Then do day 1 of `PLAN.md`.
