class TrainingController:
    def __init__(self):
        self.strategy_history = []
        self.current_patch    = ""

    def analyze(self, score: float, breakdown: dict) -> str:
        patches = []

        cat = breakdown.get("category_score", 1.0)
        pri = breakdown.get("priority_score",  1.0)
        res = breakdown.get("response_score",  1.0)
        esc = breakdown.get("escalation_score",1.0)

        if cat < 0.4:
            patches.append(
                "You are misclassifying ticket categories. "
                "Re-read: billing/technical/general/security/escalation."
            )
        if pri < 0.4:
            patches.append(
                "Your priority scoring is wrong. "
                "Remember: enterprise + outage = critical always."
            )
        if res < 0.4:
            patches.append(
                "Your responses are too short or generic. "
                "Write detailed, professional, empathetic replies."
            )
        if esc < 0.4:
            patches.append(
                "You are under-escalating. "
                "Security issues and billing disputes need human review."
            )

        patch = " ".join(patches) if patches else "Performance good. Maintain approach."
        self.current_patch = patch
        self.strategy_history.append({"score": score, "patch": patch})
        return patch

    def get_patch(self) -> str:
        return self.current_patch

    def summary(self) -> list:
        return self.strategy_history