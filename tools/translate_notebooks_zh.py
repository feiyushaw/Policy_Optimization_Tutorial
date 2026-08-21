import json
import re
from pathlib import Path

NOTEBOOKS = [
    "1_policy_optimization_introduction.ipynb",
    "2_policy_gradient.ipynb",
    "3_actor_critic.ipynb",
    "4_deterministic_policy_gradient.ipynb",
    "ex1_evolutionary_policy_optimization.ipynb",
    "ex2_actor_critic.ipynb",
    "ex3_td3.ipynb",
]

JP_RE = re.compile(r"[\u3040-\u30ff]")


def main():
    remaining = []
    for name in NOTEBOOKS:
        path = Path(name)
        data = json.loads(path.read_text(encoding="utf-8"))
        text = json.dumps(data, ensure_ascii=False)
        if JP_RE.search(text):
            remaining.append(name)
        print("OK JSON:", name)

    report = [
        "Policy Optimization Tutorial Chinese localization report",
        "========================================================",
        f"Notebooks checked: {len(NOTEBOOKS)}",
        f"Notebooks containing hiragana/katakana: {len(remaining)}",
        "",
    ]
    report.extend(remaining)
    Path("translation_report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")

    if remaining:
        raise SystemExit("Japanese text remains; see translation_report.txt")


if __name__ == "__main__":
    main()
