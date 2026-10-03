#!/usr/bin/env bash
# Publish these prepared files to an existing EMPTY private GitHub repository.
# Requires Git authentication to https://github.com/GiorgosPaspa.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
URL="https://github.com/GiorgosPaspa/perception-guided-robotic-manipulation.git"
if [ -d .git ]; then
  echo "This folder already has Git history. Refusing to overwrite it." >&2
  exit 1
fi
printf 'Before proceeding, confirm that %s exists and is PRIVATE.\n' "$URL"
read -r -p 'Have you created the empty PRIVATE repository, and verified both contributors can share it there? [y/N] ' answer
case "$answer" in y|Y|yes|YES) ;; *) echo 'Cancelled'; exit 1;; esac
git init -b main
git add .
git commit -m "Add ROS 2 perception-guided manipulation project"
git remote add origin "$URL"
git push --set-upstream origin main
echo "Published to https://github.com/GiorgosPaspa/perception-guided-robotic-manipulation"
