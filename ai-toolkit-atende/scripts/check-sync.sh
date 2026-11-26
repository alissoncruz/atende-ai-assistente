#!/usr/bin/env bash
# Fail when the product .cursor copy drifts from the toolkit source.
set -euo pipefail

SOURCE="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-$(cd "$SOURCE/.." && pwd)}"

diff -ru "$SOURCE/.cursor/rules" "$DEST/.cursor/rules"
diff -ru "$SOURCE/.cursor/skills" "$DEST/.cursor/skills"
diff -ru "$SOURCE/.cursor/hooks" "$DEST/.cursor/hooks"
diff -u "$SOURCE/.cursor/hooks.json" "$DEST/.cursor/hooks.json"
echo "cursor copy matches toolkit"
