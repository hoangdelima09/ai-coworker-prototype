def supervisor_check(state: dict, user_message: str) -> str:
    message = user_message.lower()

    direct_answer_requests = [
        "give me",
        "just give",
        "full answer",
        "answer"
    ]

    jailbreak_requests = [
        "hidden prompt",
        "system prompt",
        "evaluation logic",
        "ignore previous instructions"
    ]

    if any(phrase in message for phrase in jailbreak_requests):
        return "safety_response"

    if any(phrase in message for phrase in direct_answer_requests):
        state["repetition_count"] += 1

    if state["repetition_count"] >= 2:
        return "structured_hint"

    return "normal"