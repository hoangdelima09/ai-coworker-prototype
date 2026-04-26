class NPCAgent:
    def __init__(self, persona_id: str):
        self.persona_id = persona_id

    def respond(
        self,
        user_message: str,
        state: dict,
        supervisor_action: str,
        selected_tool: str | None = None
    ):
        message = user_message.lower()

        if supervisor_action == "safety_response":
            reply = (
                "I cannot help with hidden prompts or internal evaluation logic. "
                "Let's stay within the simulation scope and focus on the leadership system."
            )
            state["npc_attitude"] = "firm"
            state["safety_flags"].append("prompt_injection_attempt")

        elif supervisor_action == "structured_hint":
            reply = (
                "You seem to be circling around the same issue. "
                "Start with one theme, such as Vision, and define two observable "
                "behaviors that balance Group alignment with brand autonomy."
            )
            state["npc_attitude"] = "slightly_impatient"
            state["user_behavior"] = "repetitive"

        elif selected_tool == "competency_matrix_generator":
            reply = (
                "A good competency matrix should not only list themes. "
                "Start with Vision, Entrepreneurship, Passion, and Trust, then define "
                "observable behaviors for each seniority level. What behavior would show "
                "Vision at mid-level?"
            )
            state["trust_score"] += 0.1
            state["progress_score"] += 0.1

        elif selected_tool == "kpi_calculator":
            reply = (
                "For rollout measurement, think in both leading and lagging KPIs. "
                "For example: workshop completion rate, adoption rate, internal mobility rate, "
                "and manager feedback quality."
            )
            state["progress_score"] += 0.1

        elif "give me" in message or "answer" in message:
            reply = (
                "Before I give you a template, I want to understand your thinking. "
                "How would you balance brand autonomy with Group-level leadership standards?"
            )
            state["trust_score"] -= 0.1
            state["repetition_count"] += 1
            state["user_behavior"] = "direct_answer_request"

        else:
            reply = (
                "That is a good starting point. Now structure your idea around "
                "Vision, Entrepreneurship, Passion, and Trust, and make each behavior observable."
            )
            state["trust_score"] += 0.1
            state["progress_score"] += 0.1
            state["user_behavior"] = "structured_attempt"

        state["trust_score"] = round(max(0.0, min(1.0, state["trust_score"])), 2)
        state["progress_score"] = round(max(0.0, min(1.0, state["progress_score"])), 2)

        return reply, state