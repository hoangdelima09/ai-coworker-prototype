# AI Co-worker Engine Prototype

This repository contains a minimal prototype for the Edtronaut AI Engineer Intern take-home assignment.

## Focus

The prototype focuses on one AI co-worker:

**Gucci Group CHRO**

The CHRO guides the learner in designing a group-level leadership system across luxury brands while balancing Group alignment with brand autonomy.

## Features

- Persona-based NPC Agent
- Supervisor Agent for stuck detection
- Simple memory state tracking
- Tool routing logic
- Safety flag handling
- Structured input/output format

## Project Structure

```text
ai-coworker-prototype/
├── main.py
├── agents/
│   ├── npc_agent.py
│   └── supervisor_agent.py
├── memory/
│   └── state_store.py
├── tools/
│   └── tool_router.py
├── data/
│   └── gucci_context.md
└── README.md
```

## Run

```bash
python main.py
```

or:

```bash
python3 main.py
```

## Example Input

```json
{
  "persona_id": "gucci_chro",
  "user_message": "Can you just give me the competency model?"
}
```

## Example Output

```json
{
  "assistant_message": "Before I give you a template...",
  "state_update": {
    "simulation_id": "gucci_hrm",
    "persona_id": "gucci_chro",
    "current_module": "competency_model_design",
    "user_progress": "early_draft",
    "user_behavior": "direct_answer_request",
    "npc_attitude": "supportive",
    "trust_score": 0.5,
    "progress_score": 0.2,
    "repetition_count": 1,
    "safety_flags": []
  },
  "safety_flags": []
}
```

## Notes

This is a simplified prototype. It demonstrates the core logic of the AI Co-worker Engine, including persona behavior, memory state, supervisor intervention, tool routing, and safety handling.