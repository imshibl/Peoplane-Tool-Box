import re

english_words = set(
    [
        "summary",
        "objective",
        "about",
        "me",
        "experience",
        "skills",
        "education",
        "qualifications",
        "achievements",
        "accomplishments",
        "professional",
        "profile",
        "background",
        "work",
        "history",
        "employment",
        "expertise",
        "interests",
        "certifications",
        "projects",
        "publications",
        "languages",
        "technologies",
        "awards",
        "honors",
        "leadership",
        "references",
        "contact",
        "responsibilities",
        "roles",
        "responsibility",
        "objectives",
        "goal",
        "mission",
        "vision",
        "mission statement",
        "training",
        "courses",
        "conferences",
        "seminars",
        "webinars",
        "patents",
        "skills matrix",
        "strengths",
        "weaknesses",
        "hobbies",
        "volunteer",
        "extracurricular",
        "affiliations",
        "memberships",
        "professional development",
        "public speaking",
        "consulting",
        "industry knowledge",
        "industry experience",
        "core competencies",
        "qualifications summary",
        "professional summary",
        "executive summary",
        "career summary",
        "career objective",
        "personal statement",
        "workshop",
        "work experience",
        "job history",
        "accomplishments",
        "goals",
        "achievements",
        "project history",
        "research",
    ]
)


def is_valid_text(text, nlp):
    # Check if text is None
    if text is None:
        return False

    # Process the text using spaCy
    doc = nlp(
        text.lower() if text else ""
    )  # Convert to lowercase for case-insensitive comparison

    # Check if the length of the processed text is greater than 3 characters
    if len(doc.text) < 5:
        return False

    # Check if any tokens in the processed text are in the list of common English words
    valid_words = [token.text for token in doc if token.text in english_words]

    # If there are valid English words, consider the text valid
    return len(valid_words) > 0


def clean_name(name):
    if name is None:
        return None
    if len(name.strip()) == 0:
        return None

    # Remove extra spaces between letters
    cleaned_name = re.sub(r"\s(?=[A-Z])", "", name)

    return cleaned_name.replace("\n", "").strip()
