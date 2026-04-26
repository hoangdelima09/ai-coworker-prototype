_STATE = {}


def load_state(persona_id: str) -> dict:
    if persona_id not in _STATE:
        _STATE[persona_id] = {
            "simulation_id": "gucci_hrm",
            "persona_id": persona_id,
            "current_module": "competency_model_design",
            "user_progress": "early_draft",
            "user_behavior": "neutral",
            "npc_attitude": "supportive",
            "trust_score": 0.6,
            "progress_score": 0.2,
            "repetition_count": 0,
            "safety_flags": []
        }

    return _STATE[persona_id]


def save_state(persona_id: str, state: dict):
    _STATE[persona_id] = state