import json
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

def load_log(path: str) -> list:
    entries = []
    with open(path) as f:
        for line in f:
            entries.append(json.loads(line.strip()))
    return entries

def bar_chart(val: float, width: int = 30) -> str:
    filled = int(val * width)
    empty = width - filled
    
    # Color coding based on success threshold (0.6)
    color = "green" if val >= 0.6 else ("yellow" if val >= 0.4 else "red")
    
    return f"[{color}]{'#' * filled}[/][dim]{'-' * empty}[/] {val:.3f}"

def plot(log_path: str):
    entries = load_log(log_path)
    if not entries:
        print("Log is empty.")
        return

    scores  = [e["score"] for e in entries]
    tasks   = [e["task"]  for e in entries]
    avg_score = sum(scores) / len(scores) if scores else 0

    console = Console()
    
    # 1. Title Panel
    title = Text(f"Training Ground — Reward Dashboard\n", style="bold blue", justify="center")
    title.append(f"Log: {log_path}\nTotal Steps: {len(scores)}\nOverall Avg: ", style="white")
    
    avg_color = "bold green" if avg_score >= 0.6 else "bold red"
    title.append(f"{avg_score:.3f}", style=avg_color)
    
    console.print()
    console.print(Panel(title, border_style="blue", padding=(1, 2)))
    console.print()

    # 2. Step Table
    step_table = Table(title="Score per Step (Threshold: 0.6)", show_header=True, header_style="bold magenta")
    step_table.add_column("Step", justify="right", style="cyan")
    step_table.add_column("Task", style="white")
    step_table.add_column("Reward", justify="left")

    for i, e in enumerate(entries):
        step = str(i + 1)
        task_name = e["task"]
        val = e["score"]
        step_table.add_row(step, task_name, bar_chart(val))

    console.print(Align.center(step_table))
    console.print()

    # 3. Task Averages Table
    task_scores = {}
    for e in entries:
        task_scores.setdefault(e["task"], []).append(e["score"])
    
    task_avgs = {t: sum(v)/len(v) for t, v in task_scores.items()}

    avg_table = Table(title="Avg Score per Task", show_header=True, header_style="bold magenta")
    avg_table.add_column("Task", style="white")
    avg_table.add_column("Avg Reward", justify="left")

    for t, val in task_avgs.items():
        avg_table.add_row(t, bar_chart(val))

    console.print(Align.center(avg_table))
    console.print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dashboard.py runs/logs/your_log.jsonl")
    else:
        plot(sys.argv[1])