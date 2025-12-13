import json
import os
import random
from datetime import datetime

STATE_FILE = "state.json"
IDEAS_FILE = "generated_ideas.json"
LOG_FILE = "run_logs.json"

CATEGORIES = ["health", "finance", "education", "productivity", "social", "ai", "sustainability"]

TEMPLATES = {
    "health": ["AI symptom tracker", "Mental wellness companion", "Medication reminder", "Fitness planner"],
    "finance": ["Budget tracker with AI", "Investment analyzer", "Bill splitter", "Savings goal tracker"],
    "education": ["Adaptive learning app", "Language learning tool", "Study group coordinator", "Flashcard maker"],
    "productivity": ["Smart task manager", "Focus timer", "Meeting scheduler", "Habit tracker"],
    "ai": ["Personal AI assistant", "Document analyzer", "Code reviewer", "Creative writing partner"],
    "sustainability": ["Carbon footprint tracker", "Sustainable product scanner", "Energy optimizer"]
}

def load_json(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def main():
    print("🤖 AI FACTORY RUNNING")
    
    state = load_json(STATE_FILE, {"runs": 0, "last_run": None})
    ideas = load_json(IDEAS_FILE, [])
    
    # Generate idea
    cat = random.choice(CATEGORIES)
    desc = random.choice(TEMPLATES.get(cat, ["Innovative app"]))
    
    idea = {
        "id": len(ideas) + 1,
        "name": f"{cat.title()} App #{len(ideas)+1}",
        "description": desc,
        "category": cat,
        "generated_at": datetime.utcnow().isoformat(),
        "priority": random.randint(1, 100)
    }
    
    ideas.append(idea)
    save_json(IDEAS_FILE, ideas)
    
    state["runs"] += 1
    state["last_run"] = datetime.utcnow().isoformat()
    save_json(STATE_FILE, state)
    
    print(f"✅ Generated: {idea['description']}")
    print(f"📊 Total ideas: {len(ideas)} | Runs: {state['runs']}")

if __name__ == "__main__":
    main()
