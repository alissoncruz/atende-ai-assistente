#!/usr/bin/env python3
"""Keep simple tasks off expensive models.

pre-tool rewrites a Task call that names an expensive model.
subagent-start denies the spawn when the resolved model is still expensive.
A task may use an expensive model only when its text has a marker on its own line:
  complexidade: alta
  modelo-pedido
"""

from __future__ import annotations

import json
import re
import sys

CHEAP_MODEL = "composer-2.5"
MARKERS = {"complexidade: alta", "modelo-pedido"}
EXPENSIVE_FAMILY = ("opus", "fable", "gpt-5")
EFFORT = re.compile(r"(^|-)(xhigh|max)($|-)")
FAST = re.compile(r"(^|-)fast($|-)")
SONNET_HIGH = re.compile(r"sonnet.*(?:^|-)high(?:$|-)|(?:^|-)high(?:$|-).*sonnet")


def is_expensive(model: str) -> bool:
    slug = model.strip().lower()
    if not slug or slug == "inherit":
        return False
    if FAST.search(slug) or EFFORT.search(slug):
        return True
    if any(token in slug for token in EXPENSIVE_FAMILY):
        return True
    return bool(SONNET_HIGH.search(slug))


def allows_expensive(text: str) -> bool:
    for line in text.splitlines():
        if line.strip().lower() in MARKERS:
            return True
    return False


def allow() -> dict:
    return {"permission": "allow"}


def task_text(payload: dict) -> str:
    chunks = [str(payload.get(key) or "") for key in ("prompt", "description", "task")]
    nested = payload.get("tool_input")
    if isinstance(nested, dict):
        chunks.extend(str(nested.get(key) or "") for key in ("prompt", "description", "task"))
    return "\n".join(chunks)


def decide(mode: str, payload: dict) -> dict:
    if mode == "pre-tool":
        tool_input = payload.get("tool_input")
        if not isinstance(tool_input, dict):
            return allow()
        model = str(tool_input.get("model") or "")
        if is_expensive(model) and not allows_expensive(task_text(payload)):
            updated = dict(tool_input)
            updated["model"] = CHEAP_MODEL
            return {
                "permission": "allow",
                "agent_message": (
                    f"Tarefa simples não usa modelo caro ({model}). "
                    f"O Task segue com {CHEAP_MODEL}."
                ),
                "updated_input": updated,
            }
        return allow()

    if mode == "subagent-start":
        model = str(payload.get("subagent_model") or "")
        if is_expensive(model) and not allows_expensive(str(payload.get("task") or "")):
            return {
                "permission": "deny",
                "user_message": (
                    "Tarefa simples não usa modelo caro "
                    f"({model}). Refaça no turno atual ou com {CHEAP_MODEL}. "
                    "Para fronteira entre módulos ou bug sem causa óbvia, "
                    "marque a tarefa com a linha 'complexidade: alta'."
                ),
            }
        return allow()

    return allow()


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        payload = {}
    if not isinstance(payload, dict):
        payload = {}
    json.dump(decide(mode, payload), sys.stdout)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
