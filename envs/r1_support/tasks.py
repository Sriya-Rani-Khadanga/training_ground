TASKS = [
    # ── EASY ──────────────────────────────────────────────────────────────
    {
        "task_name": "easy_billing_refund",
        "input": (
            "Ticket #1001\n"
            "Subject: Wrong charge on my account\n"
            "Body: Hi, I was charged twice for my subscription this month. "
            "Please refund the extra charge ASAP.\n"
            "Customer tier: free\n"
            "Sentiment: frustrated"
        ),
        "expected": {
            "category": "billing",
            "priority": "medium",
            "escalate": False,
            "response_hints": ["refund", "charge", "apologize", "account"],
        },
        "breakdown_weights": {},
    },
    {
        "task_name": "easy_password_reset",
        "input": (
            "Ticket #1002\n"
            "Subject: Can't log in\n"
            "Body: I forgot my password and the reset email isn't arriving.\n"
            "Customer tier: free\n"
            "Sentiment: neutral"
        ),
        "expected": {
            "category": "technical",
            "priority": "low",
            "escalate": False,
            "response_hints": ["password", "reset", "email", "steps"],
        },
        "breakdown_weights": {},
    },
    {
        "task_name": "easy_general_inquiry",
        "input": (
            "Ticket #1003\n"
            "Subject: What plans do you offer?\n"
            "Body: I'm interested in upgrading. Can you tell me about pricing?\n"
            "Customer tier: free\n"
            "Sentiment: positive"
        ),
        "expected": {
            "category": "general",
            "priority": "low",
            "escalate": False,
            "response_hints": ["plan", "pricing", "upgrade", "features"],
        },
        "breakdown_weights": {},
    },

    # ── MEDIUM ────────────────────────────────────────────────────────────
    {
        "task_name": "medium_pro_billing_dispute",
        "input": (
            "Ticket #2001\n"
            "Subject: Disputing invoice #INV-8823\n"
            "Body: We were billed for 50 seats but only have 30 active users. "
            "This has happened two months in a row. We need a credit.\n"
            "Customer tier: pro\n"
            "Sentiment: angry"
        ),
        "expected": {
            "category": "billing",
            "priority": "high",
            "escalate": True,
            "response_hints": ["invoice", "credit", "seats", "investigate", "apologize"],
        },
        "breakdown_weights": {},
    },
    {
        "task_name": "medium_technical_integration",
        "input": (
            "Ticket #2002\n"
            "Subject: API returning 403 on all endpoints\n"
            "Body: Our integration broke yesterday. Every API call returns 403 "
            "Forbidden. Our API key is valid and hasn't changed.\n"
            "Customer tier: pro\n"
            "Sentiment: frustrated"
        ),
        "expected": {
            "category": "technical",
            "priority": "high",
            "escalate": False,
            "response_hints": ["403", "API", "key", "permissions", "investigate"],
        },
        "breakdown_weights": {},
    },
    {
        "task_name": "medium_security_suspicious",
        "input": (
            "Ticket #2003\n"
            "Subject: Suspicious login attempts on our account\n"
            "Body: We've noticed 15 failed login attempts from an unknown IP "
            "in the last hour. We think someone is trying to brute-force us.\n"
            "Customer tier: pro\n"
            "Sentiment: alarmed"
        ),
        "expected": {
            "category": "security",
            "priority": "high",
            "escalate": True,
            "response_hints": ["security", "IP", "block", "team", "password", "2FA"],
        },
        "breakdown_weights": {},
    },

    # ── HARD ──────────────────────────────────────────────────────────────
    {
        "task_name": "hard_enterprise_outage",
        "input": (
            "Ticket #3001\n"
            "Subject: CRITICAL — Full platform outage affecting 500 users\n"
            "Body: Our entire team is locked out of the platform. "
            "We have a board presentation in 2 hours. SLA breach imminent. "
            "This is unacceptable. We need immediate escalation.\n"
            "Customer tier: enterprise\n"
            "Sentiment: furious"
        ),
        "expected": {
            "category": "technical",
            "priority": "critical",
            "escalate": True,
            "response_hints": [
                "outage", "escalate", "team", "SLA", "priority",
                "engineer", "board", "immediate"
            ],
        },
        "breakdown_weights": {},
    },
    {
        "task_name": "hard_enterprise_data_breach",
        "input": (
            "Ticket #3002\n"
            "Subject: Possible data breach — customer PII exposed\n"
            "Body: Our security team detected that customer records may have "
            "been accessed without authorisation last night. "
            "We need your security team on a call within 30 minutes.\n"
            "Customer tier: enterprise\n"
            "Sentiment: critical"
        ),
        "expected": {
            "category": "security",
            "priority": "critical",
            "escalate": True,
            "response_hints": [
                "breach", "security", "team", "PII", "escalate",
                "investigate", "compliance", "30 minutes"
            ],
        },
        "breakdown_weights": {},
    },
    {
        "task_name": "hard_complex_sla_billing",
        "input": (
            "Ticket #3003\n"
            "Subject: SLA violation + billing error + service degradation\n"
            "Body: For the past 72 hours our uptime has been 94%% against "
            "a contracted 99.9%% SLA. Additionally we've been overbilled by "
            "$4,200. We are formally requesting SLA credits and a corrected "
            "invoice. Legal may be involved if not resolved by EOD.\n"
            "Customer tier: enterprise\n"
            "Sentiment: hostile"
        ),
        "expected": {
            "category": "escalation",
            "priority": "critical",
            "escalate": True,
            "response_hints": [
                "SLA", "credit", "invoice", "uptime", "legal",
                "escalate", "account manager", "EOD", "72 hours"
            ],
        },
        "breakdown_weights": {},
    },
]