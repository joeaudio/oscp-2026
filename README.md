# OSCP+ practical study, 2026

Original, public-safe study material for a compressed run from **17 November to
19 December 2026**. The target is to finish the study pack by 19 December; no
exam booking or pass claim is implied. Work only on your own local lab or an
explicitly authorized training target. This is a practice guide, not OffSec
course content or a replacement for PEN-200 labs.

## Start here

1. Read [SETUP.md](SETUP.md), [PLAN.md](PLAN.md), then the [lesson index](oscp-notes/INDEX.md).
2. Run `python3 labs/miniweb.py` and complete the local exercises in
   [labs/README.md](labs/README.md). Only Python 3 is required.
3. Work through the lesson matching the daily plan. Each lesson has a worked
   example, a task to attempt unaided, hints, and a check.
   [STATE.md](STATE.md) gives the first unaided exercise and current limits.
4. Copy [oscp-work/host-template-dir/target.md](oscp-work/host-template-dir/target.md)
   into ignored `oscp-work/targets/<lab>/target.md` for each authorized host.
5. Draft a report with [lab-report/template.md](lab-report/template.md).
   Use [exam-report/template.md](exam-report/template.md) as a practice layout;
   recheck OffSec's live requirements before any real exam.
6. Finish the [timed capstones](CAPSTONES.md) and score only work you actually
   demonstrated with [ASSESSMENT.md](ASSESSMENT.md).

## Layout

| Folder | Purpose |
| --- | --- |
| `oscp-notes/` | Original tutorials, commands, examples, challenges and checks |
| `oscp-work/` | Public host template; `targets/` and `evidence/` stay local and ignored |
| `lab-report/` | Reproducible practice finding template |
| `exam-report/` | Practice report outline; no real exam data |
| `oscp-scripts/` | Small, reviewed helper for a new target folder |
| `labs/` | Loopback-only synthetic web lab and self-checks |
| `fixtures/` | Invented output for offline interpretation drills |

The structure follows the useful separation in the supplied `oscp-master.zip`:
notes, per-host work, scripts, and reports. The source archive contains legacy
lab/VPN/auth and report material. It was inspected for layout only, not
extracted into this project. [SOURCE-ANALYSIS.md](SOURCE-ANALYSIS.md) records
the mapping. Everything published here is newly written or invented test data.

## Exam boundaries

As checked **17 November 2026**, the [OSCP+ Exam Guide](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide)
describes three stand-alone hosts and one three-host AD set, a 23h45m exam,
and strict report/proof requirements. It prohibits AI chatbots/LLMs during
the exam, automatic exploitation such as SQLmap, spoofing, mass vulnerability
scanners, and commercial tools; Metasploit/Meterpreter are restricted to one
chosen target. From **1 December 2026 08:00 GMT**, [scaled scoring](https://help.offsec.com/hc/en-us/articles/54589877508884-OSCP-Equated-Scaled-Scoring-FAQ)
replaces the fixed raw-point pass threshold for new attempts. Check the live
guide and exam control panel before using any technique on an exam. This repo
is for preparation; do not use an AI assistant during an active exam.

Private learning-platform files, VPN profiles, pull secrets, real credentials,
flags, screenshots, scans, and target output belong outside Git. `.gitignore`
is a guardrail, not a substitute for inspecting `git diff --cached` before push.

## Reproduce

```sh
git clone https://github.com/joeaudio/oscp-2026.git
cd oscp-2026
python3 -m unittest discover -s labs -p 'test_*.py'
python3 -m unittest discover -s tools -p 'test_*.py'
python3 labs/miniweb.py
```

No installer runs at startup. The local lab binds only to `127.0.0.1:8765`.
For full compromise practice, use your own authorized OffSec/PG/HTB lab; this
public repository does not include proprietary machines or private solutions.
