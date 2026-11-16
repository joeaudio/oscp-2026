# Reference structure audit

Reference: user-supplied `~/Downloads/oscp-master.zip`, inspected 17 November
2026. Archive integrity test passed: 2,652 entries, about 150 MB uncompressed.
The requested Git URL `https://github.com/e-noodle/oscp` required authentication
from this CLI; the supplied ZIP was used for structure inspection. No script
from the ZIP was executed, and the archive was not extracted into this repo.

| Reference folder | Useful role | This repo |
| --- | --- | --- |
| `oscp-notes/` | Method and command notes | `oscp-notes/` original tutorials |
| `oscp-work/` | Per-host evidence and reproducible path | Public host template; actual work ignored |
| `lab-report/`, `exam-report/` | Markdown reports | Fresh public-safe templates |
| `oscp-scripts/` | Workflow helpers | One small reviewed helper |
| `pandoc-tools/` | PDF generation | Plain Markdown; optional Pandoc via existing Kali setup |
| `SecLists/`, `Veil/`, `PrivEsc/` | Third-party tools | Not bundled; install/use only when needed and permitted |

The archive's README credits another blog for parts of its text and the ZIP
contains old course, exam, VPN and authentication artifacts. Those files are
unsuitable for a public study repo. The public format keeps the useful folder
separation while excluding copied material, real target data, and credentials.
