TASKS = [
    # EASY TASKS
    {
        "task_name": "High Deviation Call Arbitrage",
        "input": "pcp_deviation: 1.25, strike: 22000, expiry_days: 7, iv: 15.5, spot_price: 22100, call_price: 250, put_price: 140, transaction_cost: 0.2",
        "expected": {
            "action": "BUY_CALL",
            "reasoning": "Significant PCP deviation of 1.25 with low transaction costs and ample time to expiry makes this a clear arbitrage opportunity.",
            "escalate": False
        },
        "breakdown_weights": {}
    },
    {
        "task_name": "High Deviation Put Arbitrage",
        "input": "pcp_deviation: 1.15, strike: 22500, expiry_days: 6, iv: 16.0, spot_price: 22400, call_price: 180, put_price: 290, transaction_cost: 0.15",
        "expected": {
            "action": "BUY_PUT",
            "reasoning": "Strong PCP deviation above 1.0 and very low transaction costs justify a put-side entry.",
            "escalate": False
        },
        "breakdown_weights": {}
    },
    {
        "task_name": "Clear Trend Recovery",
        "input": "pcp_deviation: 1.05, strike: 21800, expiry_days: 8, iv: 14.2, spot_price: 21950, call_price: 320, put_price: 150, transaction_cost: 0.25",
        "expected": {
            "action": "BUY_CALL",
            "reasoning": "Deviation is healthy at 1.05 and costs are well within the profitable range for a 1-week expiry.",
            "escalate": False
        },
        "breakdown_weights": {}
    },
    
    # MEDIUM TASKS
    {
        "task_name": "Moderate Deviation Marginal Profit",
        "input": "pcp_deviation: 0.75, strike: 22200, expiry_days: 3, iv: 18.5, spot_price: 22250, call_price: 190, put_price: 130, transaction_cost: 0.45",
        "expected": {
            "action": "BUY_CALL",
            "reasoning": "Deviation of 0.75 is moderate, but costs of 0.45 still leave some alpha for a short-term trade.",
            "escalate": False
        },
        "breakdown_weights": {}
    },
    {
        "task_name": "Cost-Eroded Deviation",
        "input": "pcp_deviation: 0.60, strike: 22000, expiry_days: 4, iv: 17.0, spot_price: 22020, call_price: 210, put_price: 185, transaction_cost: 0.55",
        "expected": {
            "action": "HOLD",
            "reasoning": "While pcp_deviation is positive at 0.60, the transaction cost of 0.55 eats most of the potential profit, making it better to hold.",
            "escalate": False
        },
        "breakdown_weights": {}
    },
    {
        "task_name": "Short Expiry Put Setup",
        "input": "pcp_deviation: 0.85, strike: 22300, expiry_days: 2, iv: 19.2, spot_price: 22280, call_price: 145, put_price: 160, transaction_cost: 0.35",
        "expected": {
            "action": "BUY_PUT",
            "reasoning": "Good deviation of 0.85 with manageable costs for a 2-day setup.",
            "escalate": False
        },
        "breakdown_weights": {}
    },

    # HARD TASKS
    {
        "task_name": "Low Deviation STT Trap",
        "input": "pcp_deviation: 0.35, strike: 22100, expiry_days: 1, iv: 22.0, spot_price: 22110, call_price: 90, put_price: 85, transaction_cost: 0.65",
        "expected": {
            "action": "HOLD",
            "reasoning": "High risk of STT trap due to near-expiry and low pcp_deviation of 0.35. Transaction costs exceed potential alpha.",
            "escalate": True
        },
        "breakdown_weights": {}
    },
    {
        "task_name": "Expensive Execution Risk",
        "input": "pcp_deviation: 0.20, strike: 22400, expiry_days: 1, iv: 21.5, spot_price: 22390, call_price: 110, put_price: 125, transaction_cost: 0.75",
        "expected": {
            "action": "HOLD",
            "reasoning": "Extremely low deviation and very high transaction costs of 0.75 make this an STT trap candidate. Do not execute.",
            "escalate": True
        },
        "breakdown_weights": {}
    },
    {
        "task_name": "Marginal Setup Near Expiry",
        "input": "pcp_deviation: 0.45, strike: 22000, expiry_days: 1, iv: 20.0, spot_price: 22015, call_price: 130, put_price: 110, transaction_cost: 0.70",
        "expected": {
            "action": "HOLD",
            "reasoning": "pcp_deviation is too low at 0.45 to offset the 0.70 transaction cost. STT trap risk is high on expiry day.",
            "escalate": True
        },
        "breakdown_weights": {}
    }
]
