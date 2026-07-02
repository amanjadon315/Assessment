def decide(analysis):

    if analysis["out_of_scope"]:
        return {
            "action": "refuse"
        }

    intent = analysis["intent"]

    if intent == "compare":
        return {
            "action": "compare"
        }

    if intent == "refine":
        return {
            "action": "refine"
        }

    context = analysis["context"]

    if context["role"] is None:
        return {
            "action": "ask",
            "question": "What role are you hiring for?"
        }

    if context["purpose"] is None:
        return {
            "action": "ask",
            "question": "Is this assessment for hiring, development, promotion, or succession planning?"
        }

    return {
        "action": "recommend"
    }