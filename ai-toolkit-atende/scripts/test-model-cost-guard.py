#!/usr/bin/env python3
"""Feed the cost guard JSON fixtures and check the decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

GUARD = Path(__file__).resolve().parents[1] / ".cursor" / "hooks" / "model-cost-guard.py"


def run(mode: str, payload: dict) -> dict:
    completed = subprocess.run(
        [sys.executable, str(GUARD), mode],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise SystemExit(f"{mode} exited {completed.returncode}: {completed.stderr}")
    return json.loads(completed.stdout)


def expect(name: str, actual, wanted) -> None:
    if actual != wanted:
        raise SystemExit(f"{name}: got {actual!r}, want {wanted!r}")


def main() -> None:
    simple = {"prompt": "Corrigir typo no README", "description": "typo"}
    rewritten = run("pre-tool", {"tool_name": "Task", "tool_input": {**simple, "model": "claude-opus-5-5-high"}})
    expect("opus rewrite", rewritten["updated_input"]["model"], "composer-2.5")
    expect("opus keeps prompt", rewritten["updated_input"]["prompt"], simple["prompt"])

    for model in ("composer-2.5", "inherit", "grok-4.7-high", "claude-sonnet-5-5-medium", ""):
        decision = run("pre-tool", {"tool_input": {**simple, "model": model}})
        expect(f"allow {model or 'empty'}", "updated_input" in decision, False)
        expect(f"permission {model or 'empty'}", decision["permission"], "allow")

    for model in ("claude-fable-5-2-max", "gpt-5.6-sol-low", "composer-2.5-fast", "grok-4.7-xhigh", "claude-sonnet-5-5-high"):
        decision = run("pre-tool", {"tool_input": {"model": model, "prompt": "renomear campo"}})
        expect(model, decision["updated_input"]["model"], "composer-2.5")

    marked = {"model": "claude-opus-5-5-max", "prompt": "Investigar fronteira\ncomplexidade: alta"}
    decision = run("pre-tool", {"tool_input": marked})
    expect("marked stays", "updated_input" in decision, False)

    buried = {"model": "claude-opus-5-5", "prompt": "A regra diz complexidade: alta no meio da frase"}
    decision = run("pre-tool", {"tool_input": buried})
    expect("buried marker", decision["updated_input"]["model"], "composer-2.5")

    denied = run("subagent-start", {"subagent_model": "claude-opus-5-5", "task": "Ajustar um gitkeep"})
    expect("deny opus", denied["permission"], "deny")

    allowed = run(
        "subagent-start",
        {"subagent_model": "claude-opus-5-5", "task": "Desenhar a fronteira\ncomplexidade: alta"},
    )
    expect("allow marked", allowed["permission"], "allow")

    requested = run(
        "subagent-start",
        {"subagent_model": "gpt-5.6-sol-max", "task": "modelo-pedido"},
    )
    expect("allow requested", requested["permission"], "allow")

    inherit = run("subagent-start", {"subagent_model": "inherit", "task": "typo"})
    expect("inherit", inherit["permission"], "allow")

    garbage = subprocess.run(
        [sys.executable, str(GUARD), "pre-tool"],
        input="{not json",
        text=True,
        capture_output=True,
        check=False,
    )
    expect("garbage exit", garbage.returncode, 0)
    expect("garbage allow", json.loads(garbage.stdout)["permission"], "allow")

    print("model-cost-guard: ok")


if __name__ == "__main__":
    main()
