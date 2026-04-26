def should_call_tool(user_message: str) -> str | None:
    message = user_message.lower()

    if (
        "competency" in message
        or "framework" in message
        or "behavior" in message
        or "vision" in message
        or "entrepreneurship" in message
    ):
        return "competency_matrix_generator"

    if (
        "kpi" in message
        or "measurement" in message
        or "adoption" in message
        or "rollout" in message
    ):
        return "kpi_calculator"

    return None