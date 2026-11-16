# 12 — Mixed attempts, tool rules and report rehearsal

**Outcome:** complete a timed attempt without hints, then turn it into a
reproducible report. This chapter is for preparation, not an active exam.

## Tool decision before a target

Write the target, permitted network, and tool restrictions before running
anything. The [current OffSec guide](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide)
prohibits automatic exploitation tools, spoofing, mass vulnerability scanners,
commercial tools and AI chatbots/LLMs on OSCP+. Metasploit/Meterpreter may be
used against **one chosen target**; its `check` use counts. `msfvenom` and a
multi-handler have stated exceptions, but read the live guide for exact scope.
Course labs may permit more tools than the exam. AV evasion and Metasploit are
course topics, yet a manual verification path should be understood first.

## Timed mock

1. Pick a fresh authorized lab target or synthetic fixture; set a timebox.
2. Spend 15 minutes making the service map, then choose one lead at a time.
3. At each pivot, record starting access, command, output and why the next
   step follows. Do not consult a walkthrough during the attempt.
4. Reserve the last 25% of the session to reproduce, capture evidence and
   write the report. Mark unknowns honestly.
5. Afterward, compare with the lab's official solution only if permitted.
   Record one gap and one unaided repeat task for the next day.

The real exam's proof and screenshot rules are strict and can change. As of
17 November 2026, the guide requires proof contents shown from the original
location in an interactive shell with target IP visible in the screenshot,
and a detailed report sufficient for another technical reader to reproduce.
Use the exam control panel and live guide as the final authority.

## Challenge

Using only `fixtures/scan.txt`, `fixtures/linux.txt` and `fixtures/ad-paths.csv`,
produce a 45-minute mock report outline. Label each statement fact,
hypothesis or unresolved. Then complete an authorized target with no AI,
hints or walkthrough during the timed attempt.

<details><summary>Hint 1</summary>Start from the host note template; each claim needs evidence, including negative checks.</details>
<details><summary>Hint 2</summary>Separate unrelated synthetic hosts. Do not invent a single attack chain across fixtures.</details>
<details><summary>Check</summary>A credible report does not claim compromise from these fixtures alone. It gives observed service facts, candidate paths, exact missing verification, and next safe checks.</details>
