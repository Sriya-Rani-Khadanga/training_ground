def compute_reward(output: dict, expected: dict) -> float:
    # 1. action_score (weight 0.40)
    output_action = output.get("action", "")
    expected_action = expected.get("action", "")
    
    if output_action == expected_action:
        action_score = 1.0
    elif (("BUY" in output_action and "BUY" in expected_action) or 
          ("SELL" in output_action and "SELL" in expected_action)):
        action_score = 0.5
    else:
        action_score = 0.0

    # 2. reasoning_score (weight 0.30)
    output_reasoning = output.get("reasoning", "").lower()
    expected_reasoning = expected.get("reasoning", "").lower()
    
    # Extract keywords (simple split for this requirement)
    keywords = [k.strip() for k in expected_reasoning.replace(",", "").split() if len(k) > 3]
    if not keywords:
        reasoning_score = 1.0
    else:
        matched = sum(1 for kw in keywords if kw in output_reasoning)
        reasoning_score = matched / len(keywords)

    # 3. cost_awareness_score (weight 0.20)
    cost_keywords = ["stt", "cost", "transaction", "expiry"]
    risk_keywords = ["risk"]
    
    if any(kw in output_reasoning for kw in cost_keywords):
        cost_awareness_score = 1.0
    elif any(kw in output_reasoning for kw in risk_keywords):
        cost_awareness_score = 0.5
    else:
        cost_awareness_score = 0.0

    # 4. confidence_score (weight 0.10)
    confidence = output.get("confidence")
    if confidence is not None and isinstance(confidence, (int, float)) and 0.0 <= confidence <= 1.0:
        confidence_score = 1.0
    else:
        confidence_score = 0.0

    # final_score calculation
    final_score = (
        (action_score * 0.40) +
        (reasoning_score * 0.30) +
        (cost_awareness_score * 0.20) +
        (confidence_score * 0.10)
    )
    
    # Clamp to range 0.01 to 0.99
    final_score = max(0.01, min(0.99, final_score))
    
    # Store breakdown
    compute_reward.last_breakdown = {
        "action_score": action_score,
        "reasoning_score": reasoning_score,
        "cost_awareness_score": cost_awareness_score,
        "confidence_score": confidence_score
    }
    
    return float(final_score)

compute_reward.last_breakdown = {}
