from enum import Enum

from pydantic import BaseModel


class CountryEnum(str, Enum):
    USA = "USA"
    GERMANY = "GERMANY"
    FRANCE = "FRANCE"
    AUSTRALIA = "AUSTRALIA"
    INDIA = "INDIA"
    CANADA = "CANADA"
    JAPAN = "JAPAN"
    UK = "UK"
    NEW_ZEALAND = "NEW ZEALAND"


class PersonalityEnum(str, Enum):
    INTROVERT = "introvert"
    EXTROVERT = "extrovert"


class BudgetEnum(str, Enum):
    FREE = "free"
    PAID = "paid"


class MoodEnum(str, Enum):
    HAPPY = "happy"
    RELAXED = "relaxed"
    ADVENTUROUS = "adventurous"
    CURIOUS = "curious"
    ANXIOUS = "anxious"
    SAD = ("sad",)
    TENSE = ("tense",)
    EXCITED = ("excited",)
    AFRAID = ("afraid",)
    ANGRY = ("angry",)
    CONFUSED = ("confused",)


class TaskSuggestion(BaseModel):
    country: CountryEnum
    personality: PersonalityEnum
    budget: BudgetEnum
    mood: MoodEnum
