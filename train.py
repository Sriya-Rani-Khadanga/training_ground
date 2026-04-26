import json
import os
from dotenv import load_dotenv
load_dotenv()
from envs.r1_support.grader import compute_reward

from core.agent      import Agent
from core.evaluator  import Evaluator
from core.controller import TrainingController
from core.memory     import Memory
from envs.r1_support.tasks import TASKS



SYSTEM_PROMPT_BASE = """
You are an expert customer support triage agent for a SaaS company.

Your job:
1. Classify the ticket into one category: billing, technical, general, security, escalation
2. Assign priority: low, medium, high, critical
3. Write a professional customer-facing response (min 40 words)
4. Decide if human escalation is needed: true or false

SLA Rules:
- enterprise tier + any outage = critical
- pro tier + billing issue = high
- security issues always = escalate true
- free tier general questions = low

Always return ONLY valid JSON in this exact format:
{
  "category": "...",
  "priority": "...",
  "response": "...",
  "escalate": true/false
}
""".strip()


def run_training(n_iterations: int = 3, env: str = "r1_support"):
    memory     = Memory(run_name=env)
    evaluator  = Evaluator(env=env)
    controller = TrainingController()

    current_prompt = SYSTEM_PROMPT_BASE
    agent = Agent(system_prompt=current_prompt)

    print(f"\n🚀 Training on env: {env}")
    print(f"{'─' * 50}")

    for iteration in range(n_iterations):
        print(f"\n📍 Iteration {iteration + 1}/{n_iterations}")
        iter_scores = []

        for task in TASKS:
            raw = agent.run(task["input"])

            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError:
                parsed = {}

            score     = evaluator.score(parsed, task["expected"])
            breakdown = compute_reward.last_breakdown
            strategy  = controller.analyze(score, breakdown)

            memory.record(
                step     = len(memory.history),
                task     = task["task_name"],
                output   = parsed,
                score    = score,
                strategy = strategy,
            )
            iter_scores.append(score)
            print(f"  {'✅' if score >= 0.6 else '⚠️ '} {task['task_name']}: {score:.3f}")

        avg = sum(iter_scores) / len(iter_scores)
        print(f"\n  📊 Iteration {iteration+1} avg: {avg:.3f}")

        patch = controller.get_patch()
        if patch:
            agent.patch_prompt(patch)
            print(f"  🔧 Prompt patched: {patch[:80]}...")

    print(f"\n{'─' * 50}")
    print(f"🏁 Final avg score : {memory.average_score():.3f}")
    print(f"📈 Score curve     : {memory.score_curve()}")
    print(f"💾 Logs saved to   : {memory.path}")
    return memory


if __name__ == "__main__":
    run_training(n_iterations=3)