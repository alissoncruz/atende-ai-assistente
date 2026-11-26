#!/usr/bin/env bash
# Copy toolkit Cursor files into a project root. Default: the parent repo.
set -euo pipefail

SOURCE="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-$(cd "$SOURCE/.." && pwd)}"

mkdir -p "$DEST/.cursor/rules" "$DEST/.cursor/skills" "$DEST/.cursor/hooks"
rm -rf "$DEST/.cursor/rules" "$DEST/.cursor/skills" "$DEST/.cursor/hooks"
mkdir -p "$DEST/.cursor/rules" "$DEST/.cursor/skills" "$DEST/.cursor/hooks"
cp -a "$SOURCE/.cursor/rules/." "$DEST/.cursor/rules/"
cp -a "$SOURCE/.cursor/skills/." "$DEST/.cursor/skills/"
cp -a "$SOURCE/.cursor/hooks/." "$DEST/.cursor/hooks/"
cp "$SOURCE/.cursor/hooks.json" "$DEST/.cursor/hooks.json"
chmod +x "$DEST/.cursor/hooks/model-cost-guard.py"
echo "synced $SOURCE/.cursor -> $DEST/.cursor"
