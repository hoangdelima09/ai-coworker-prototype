from agents.npc_agent import NPCAgent
from agents.supervisor_agent import supervisor_check
from memory.state_store import load_state, save_state
from tools.tool_router import should_call_tool


def handle_message(persona_id: str, user_message: str):
    state = load_state(persona_id)

    supervisor_action = supervisor_check(state, user_message)
    selected_tool = should_call_tool(user_message)

    agent = NPCAgent(persona_id)

    assistant_message, updated_state = agent.respond(
        user_message=user_message,
        state=state,
        supervisor_action=supervisor_action,
        selected_tool=selected_tool
    )

    save_state(persona_id, updated_state)

    return {
        "assistant_message": assistant_message,
        "state_update": updated_state,
        "safety_flags": updated_state.get("safety_flags", [])
    }


if __name__ == "__main__":
    result = handle_message(
        persona_id="gucci_chro",
        user_message="Can you just give me the competency model?"
    )

    print(result)