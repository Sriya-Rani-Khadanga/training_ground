import json
import os
from datetime import datetime


class Memory:
    def __init__(self, run_name="run"):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs("runs/logs", exist_ok=True)
        self.path = f"runs/logs/{run_name}_{ts}.jsonl"
        self.history = []

    def record(self, step: int, task: str, output: dict,
               score: float, strategy: str):
        entry = {
            "step":      step,
            "task":      task,
            "output":    output,
            "score":     score,
            "strategy":  strategy,
            "timestamp": datetime.now().isoformat(),
        }
        self.history.append(entry)
        with open(self.path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def average_score(self) -> float:
        if not self.history:
            return 0.0
        return sum(e["score"] for e in self.history) / len(self.history)

    def score_curve(self) -> list:
        return [e["score"] for e in self.history]

    def by_iteration(self, tasks_per_iter: int) -> list:
        curve = self.score_curve()
        return [
            round(sum(curve[i:i+tasks_per_iter]) / tasks_per_iter, 4)
            for i in range(0, len(curve), tasks_per_iter)
        ]