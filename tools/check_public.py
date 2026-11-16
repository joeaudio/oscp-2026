#!/usr/bin/env python3
"""Small staged-file guard; review the staged diff yourself too."""

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BLOCKED_PARTS = {"private", "targets", "evidence", "vpn", "downloads"}
BLOCKED_SUFFIXES = {".ovpn", ".pcap", ".pcapng", ".iso", ".zip", ".7z", ".pem", ".key", ".pdf"}
TOKEN_PATTERNS = (
    re.compile(rb"(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}"),
    re.compile(rb"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(rb"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(rb'"auths"\s*:\s*\{'),
)


def problem(path, data):
    name = Path(path)
    if BLOCKED_PARTS.intersection(name.parts) or name.suffix.lower() in BLOCKED_SUFFIXES:
        return "private or binary path"
    if "pull-secret" in name.name.lower() or name.name.lower() == "auth.json":
        return "credential filename"
    if len(data) > 1_000_000 or b"\x00" in data:
        return "large or binary file"
    if any(b"-----BEGIN " + kind + b"PRIVATE KEY-----" in data
           for kind in (b"", b"RSA ", b"EC ", b"OPENSSH ")):
        return "private key block"
    if any(pattern.search(data) for pattern in TOKEN_PATTERNS):
        return "credential-like content"
    return None


def main():
    paths = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM", "-z"], cwd=ROOT
    ).split(b"\x00")
    failures = []
    for raw in filter(None, paths):
        path = raw.decode("utf-8", "surrogateescape")
        file = ROOT / path
        if file.is_symlink():
            failures.append((path, "symlink"))
            continue
        issue = problem(path, file.read_bytes())
        if issue:
            failures.append((path, issue))
    for path, issue in failures:
        print(f"BLOCKED {path}: {issue}")
    if failures:
        raise SystemExit(1)
    print(f"Staged guard passed for {len(list(filter(None, paths)))} files; inspect diff manually.")


if __name__ == "__main__":
    main()
