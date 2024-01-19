import re


class RegexPatterns:
    # Define regex patterns

    name_pattern = re.compile(r"([^\d]+?)\n")

    number_pattern = re.compile(r"\+?(\d{1,4}\s?)?(\d{3}\s?\d{2,3}\s?\d{2,4})\b")

    email_pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")

    experience_pattern = re.compile(
        r"E\s*x\s*p\s*e\s*r\s*i\s*e\s*n\s*c\s*e|E\s*X\s*P\s*E\s*R\s*I\s*E\s*N\s*C\s*E"
    )

    education_pattern = re.compile(
        r"E\s*d\s*u\s*c\s*a\s*t\s*i\s*o\s*n|E\s*D\s*U\s*C\s*A\s*T\s*I\s*O\s*N"
    )

    skills_pattern = re.compile(
        r"S\s*k\s*i\s*l\s*l\s*s|S\s*K\s*I\s*L\s*L\s*S|S\s*K\s*I\s*L\s*L|S\s*k\s*i\s*l\s*l"
    )

    country_code_pattern = re.compile(r"\(?\+(\d{1,4})\)?\s*(\d+)")

    languages_pattern = re.compile(
        r"L\s*a\s*n\s*g\s*u\s*a\s*g\s*e\s*s|L\s*A\s*N\s*G\s*U\s*A\s*G\s*E\s*S|L\s*a\s*n\s*g\s*u\s*a\s*g\s*e|L\s*A\s*N\s*G\s*U\s*A\s*G\s*E"
    )

    hobbies_and_interests_pattern = re.compile(
        r"H\s*o\s*b\s*b\s*i\s*e\s*s|H\s*O\s*B\s*B\s*I\s*E\s*S|H\s*O\s*B\s*B\s*Y|H\s*o\s*b\s*b\s*y|I\s*n\s*t\s*e\s*r\s*e\s*s\s*t\s*s|I\s*N\s*T\s*E\s*R\s*E\s*S\s*T\s*S|I\s*n\s*t\s*e\s*r\s*e\s*s\s*t|I\s*N\s*T\s*E\s*R\s*E\s*S\s*T"
    )

    certifications_pattern = re.compile(
        r"C\s*e\s*r\s*t\s*i\s*f\s*i\s*c\s*a\s*t\s*i\s*o\s*n|C\s*E\s*R\s*T\s*I\s*F\s*I\s*C\s*A\s*T\s*I\s*O\s*N|C\s*e\s*r\s*t\s*i\s*f\s*i\s*c\s*a\s*t\s*e\s*s|C\s*E\s*R\s*T\s*I\s*F\s*I\s*C\s*A\s*T\s*E\s*S|C\s*e\s*r\s*t\s*i\s*f\s*i\s*c\s*a\s*t\s*e|C\s*E\s*R\s*T\s*I\s*F\s*I\s*C\s*A\s*T\s*E"
    )

    references_pattern = re.compile(
        r"R\s*e\s*f\s*e\s*r\s*e\s*n\s*c\s*e|R\s*E\s*F\s*E\s*R\s*E\s*N\s*C\s*E"
    )

    # projects_pattern = re.compile(
    #     r"P\s*r\s*o\s*j\s*e\s*c\s*t\s*s|P\s*R\s*O\s*J\s*E\s*C\s*T\s*S|P\s*r\s*o\s*j\s*e\s*c\s*t|P\s*R\s*O\s*J\s*E\s*C\s*T"
    # )
    projects_pattern = re.compile(
        r"P\s*r\s*o\s*j\s*e\s*c\s*t\s*s|P\s*R\s*O\s*J\s*E\s*C\s*T\s*S"
    )

    honors_and_awards_pattern = re.compile(
        r"H\s*o\s*n\s*o\s*r\s*s|A\s*w\s*a\s*r\s*d\s*s|H\s*O\s*N\s*O\s*R\s*S|A\s*W\s*A\s*R\s*D\s*S"
    )

    declaration_pattern = re.compile(
        r"D\s*e\s*c\s*l\s*a\s*r\s*a\s*t\s*i\s*o\s*n|D\s*E\s*C\s*L\s*A\s*R\s*A\s*T\s*I\s*O\s*N|hereby|declare|best\s*of\s*my\s*knowledge|appreciate\s*you\s*taking\s*the\s*time\s*to\s*look\s*over\s*my\s*qualifications(?:\s*and\s*experience)?|get\s*in\s*touch\s*with\s*me|hesitate|I\s*appreciate\s*your\s*time|Thank\s*you|thank\s*you"
    )
