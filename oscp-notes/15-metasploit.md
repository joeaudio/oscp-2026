# 15 — Metasploit anatomy and restricted use

**Outcome:** understand module options and payloads without turning the
framework into a substitute for manual enumeration.

## Tutorial

An auxiliary module performs a supporting task, an exploit module attempts
initial access, and a post module acts after access. Staged payloads fetch
more code after the first stage; single payloads carry the whole action.
Review module source, options, and network behavior before running it.

In a local training VM, these commands inspect the framework only:

```text
msfconsole -q
msf6 > help
msf6 > search type:auxiliary http
msf6 > info <selected-module>
msf6 > use <selected-module>
msf6 > show options
```

Do not paste a target or run a module until scope and the current exam rule
are clear. The [OSCP+ guide](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide)
currently limits Metasploit modules and Meterpreter to one selected machine,
and even using `check` commits that choice. It allows `msfvenom` and a
multi-handler with stated conditions. Metasploit pivoting across multiple
exam targets is prohibited. Record the chosen machine privately; avoid
accidentally touching another target through a module or automation.

## Challenge

You have two authorized practice hosts. Design a manual validation path for
both, then choose one on which you would spend your single Metasploit option
in an exam-style rehearsal. Explain what `info` and `show options` tell you
before execution and what they cannot prove.

<details><summary>Hint 1</summary>Choose based on verified preconditions and expected value, not only a matching module name.</details>
<details><summary>Hint 2</summary>`check` can still contact a host and counts under the current restriction.</details>
<details><summary>Check</summary>A good plan identifies one target, confirms the module's applicability manually, records every option and keeps the other host entirely outside Metasploit modules/Meterpreter.</details>
