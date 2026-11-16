#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 || ! "$1" =~ ^[A-Za-z0-9_-]+$ ]]; then
  echo 'Usage: new-target.sh LABEL (letters, digits, underscore, hyphen)' >&2
  exit 2
fi

repo=$(cd -- "$(dirname -- "$0")/.." && pwd)
target="$repo/oscp-work/targets/$1"
if [[ -e "$target" ]]; then
  echo "Target folder already exists: $target" >&2
  exit 1
fi
mkdir -p "$target"
cp "$repo/oscp-work/host-template-dir/target.md" "$target/target.md"
echo "$target/target.md"
