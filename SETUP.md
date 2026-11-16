# Reproduce the public practice environment

The executable local lab uses only Python 3's standard library. On a fresh
Kali/Debian machine, review before installing the individual tools used in
the tutorial examples:

```sh
sudo apt-get update
xargs -r sudo apt-get -s install --no-install-recommends < config/practice-tools.txt
xargs -r sudo apt-get install --no-install-recommends < config/practice-tools.txt
python3 -m unittest discover -s labs -p 'test_*.py'
python3 -m unittest discover -s tools -p 'test_*.py'
python3 labs/miniweb.py
```

On another terminal, use `curl`, browser developer tools, or Burp Free against
`http://127.0.0.1:8765`. Stop with Ctrl-C. The lab is deliberately weak and
must remain loopback-only. No Docker, root access, external account, or
startup service is required for it.

Practice on real Windows, Linux and AD hosts requires your own authorized
course or training lab. Those machines, VPN profiles, credentials, license
keys and course files are not distributed here. Use the host template inside
the ignored `oscp-work/targets/` area:

```sh
./oscp-scripts/new-target.sh practice01
```

The new folder is local and ignored by Git. Copy the public report templates
into it before filling them. For PDF drafting, Pandoc is optional:

```sh
pandoc lab-report/template.md -o /tmp/practice-template.pdf
```

Before a public commit or push, stage only intended text files, run
`python3 tools/check_public.py`, and inspect `git diff --cached` yourself.
The guard checks common secrets, paths, binary files and size; it cannot
recognize every personal or course-specific detail.
