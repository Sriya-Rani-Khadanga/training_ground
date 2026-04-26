from envs.r1_support.grader import compute_reward as r1_grader


class Evaluator:
    def __init__(self, env: str = "r1_support"):
        self.env = env
        self._graders = {
            "r1_support": r1_grader,
            # "r2_ps": r2_grader   ← you'll add this when R2 PS is locked
        }

    def score(self, output: dict, expected: dict) -> float:
        grader_fn = self._graders.get(self.env)
        if not grader_fn:
            raise ValueError(f"No grader registered for env: {self.env}")
        return grader_fn(output, expected)

    def register(self, env_name: str, grader_fn):
        self._graders[env_name] = grader_fn
        print(f"[Evaluator] registered grader for '{env_name}'")