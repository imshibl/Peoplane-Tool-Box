import random

from fastapi import APIRouter

from ...features.suggest_tasks.tasks_database import tasks_database
from ...models.suggest_tasks_model import TaskSuggestion

router = APIRouter()


@router.post("/suggest-tasks", tags=["Tools"])
def boredom_buster_suggest_tasks(input: TaskSuggestion):
    country = input.country
    personality = input.personality
    budget = input.budget
    mood = input.mood
    # Check if the country is in the mapping
    if country in tasks_database:
        # Determine whether the user is an introvert or extrovert
        user_tasks = tasks_database[country][personality.lower()]

        # Select tasks based on budget (free or paid)
        budget_key = "free" if budget.lower() == "free" else "paid"
        selected_tasks = random.sample(
            user_tasks[budget_key][mood.lower()],
            min(3, len(user_tasks[budget_key][mood.lower()])),
        )  # Limit to 3 suggestions

        return selected_tasks
    else:
        return []
