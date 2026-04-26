from __future__ import annotations


# ── weights (must sum to 1.0) ──────────────────────────────────────────────
W_CATEGORY   = 0.40
W_PRIORITY   = 0.20
W_ESCALATION = 0.10
W_RESPONSE   = 0.30

VALID_CATEGORIES = {"billing", "technical", "general", "security", "escalation"}
VALID_PRIORITIES = {"low", "medium", "high", "critical"}


def _clamp(val: float) -> float:
    """Phase 2 compliance — no zero/one signals."""
    return max(0.01, min(0.99, val))


def _score_category(output: dict, expected: dict) -> float:
    got  = str(output.get("category", "")).strip().lower()
    want = str(expected.get("category", "")).strip().lower()
    return 1.0 if got == want else 0.0


def _score_priority(output: dict, expected: dict) -> float:
    got  = str(output.get("priority", "")).strip().lower()
    want = str(expected.get("priority", "")).strip().lower()
    if got == want:
        return 1.0
    # partial credit for adjacent priorities
    order = ["low", "medium", "high", "critical"]
    if got in order and want in order:
        diff = abs(order.index(got) - order.index(want))
        if diff == 1:
            return 0.5
    return 0.0


def _score_escalation(output: dict, expected: dict) -> float:
    got  = output.get("escalate")
    want = expected.get("escalate")
    if isinstance(got, str):
        got = got.lower() == "true"
    return 1.0 if bool(got) == bool(want) else 0.0


def _score_response(output: dict, expected: dict) -> float:
    response = str(output.get("response", ""))
    if len(response) < 20:
        return 0.0

    score = 0.0

    # length score (up to 0.20) — matches your R1 spec
    if len(response) >= 100:
        score += 0.20
    elif len(response) >= 40:
        score += 0.10

    # keyword matching (up to 0.10) — matches your R1 spec
    hints = expected.get("response_hints", [])
    response_lower = response.lower()
    if hints:
        matched = sum(1 for h in hints if h.lower() in response_lower)
        score += 0.10 * (matched / len(hints))
    else:
        score += 0.10

    # scale to full 0-1 range for grader
    return min(score / 0.30, 1.0)


def compute_reward(output: dict, expected: dict) -> float:
    """
    Main grader entry point.
    Returns a float in [0.01, 0.99] — Phase 2 compliant.
    Also returns breakdown as a side-channel via compute_reward.breakdown.
    """
    if not output:
        return 0.01

    cat = _score_category(output, expected)
    pri = _score_priority(output, expected)
    esc = _score_escalation(output, expected)
    res = _score_response(output, expected)

    raw = (
        W_CATEGORY   * cat +
        W_PRIORITY   * pri +
        W_ESCALATION * esc +
        W_RESPONSE   * res
    )

    # attach breakdown so controller can inspect sub-scores
    compute_reward.last_breakdown = {
        "category_score":   _clamp(cat),
        "priority_score":   _clamp(pri),
        "escalation_score": _clamp(esc),
        "response_score":   _clamp(res),
    }

    return _clamp(raw)


# initialise attribute so it always exists
compute_reward.last_breakdown = {}