from .utils.suggetions import suggetions


class ResumeSuggetions:
    def generateCustomResumeSuggestions(
        name,
        mobile_number,
        email,
        country_code,
        score,
        experience,
        education,
        skills,
        languages,
        hobbies_and_interests,
        references,
        declaration,
        projects,
        certifications,
    ):
        custom_suggestions = []

        if (
            not name
            or name == ""
            or name == " "
            or name == "\n "
            or name == "\n"
            or len(name) < 5
        ):
            custom_suggestions.append(suggetions["name"])

        if (
            not mobile_number
            or mobile_number == ""
            or not country_code
            or country_code == ""
        ):
            custom_suggestions.append(suggetions["mobile_number"])
        if not email or email == "":
            custom_suggestions.append(suggetions["email"])

        if (
            not experience
            or not education
            or not skills
            or not languages
            or not hobbies_and_interests
            or not references
            or not declaration
            or not projects
            or not certifications
        ):
            custom_suggestions.append(suggetions["sections"])

        if score < 80:
            custom_suggestions.append(suggetions["extraction"])

        return custom_suggestions

    def suggest_platforms_to_create_cv(score):
        if score > 70:
            return None
        else:
            return {
                "suggestion": "Your CV have a lot of room for improvement. Explore reputable online platforms to create professional resumes easily. Choose platforms that offer user-friendly interfaces, a variety of templates with ATS friendly features and export options for different file formats.",
                "platforms": [
                    "Canva",
                    "LinkedIn",
                    "Indeed",
                    "Europass",
                    "Zety",
                    "Resume.com",
                    "NovoResume",
                    "Overleaf",
                ],
            }

    def message_based_on_page_count(page_count, score):
        if score > 70:
            if page_count == 1:
                message = (
                    "Fantastic! Your 1-page resume is perfectly aligned with the expectations for entry-level candidates. Focus on showcasing key achievements, skills, and education to make a strong impression.",
                )

            elif page_count == 2:
                message = (
                    "Great! Your 2-page resume aligns well with the expectations for mid-level professionals. Ensure you emphasize your comprehensive work experience and notable accomplishments to make a strong impact",
                )

            else:
                message = "Your {}-page resume suggests a rich professional history. Ensure that each section contributes to your overall narrative and showcases your key achievements, skills, and experiences. Consider streamlining if possible to maintain reader engagement.".format(
                    page_count
                )

        else:
            if page_count == 1:
                message = (
                    "Your 1-page resume presents an opportunity for substantial enhancements. Consider conducting a thorough review, placing emphasis on highlighting notable achievements and ensuring that each section contributes cohesively to a compelling professional narrative.",
                )

            elif page_count == 2:
                message = (
                    "Your 2-page resume could benefit from significant improvements. Consider a comprehensive review, emphasizing notable accomplishments and ensuring each section contributes to a strong professional narrative.",
                )

            else:
                message = (
                    "Your {}-page resume indicates a need for major changes. Undertake a thorough revision, ensuring each section is essential and contributes to a cohesive narrative. Consider streamlining if certain details can be condensed without losing impact.".format(
                        page_count
                    ),
                )

        return message

    def about_page_number_message():
        return {
            "entry_level": "For entry-level resumes, it is recommended to keep it concise and limit it to 1 page. Focus on highlighting key skills, education, and relevant experiences.",
            "mid_level": "For mid-level resumes, a length of maximum 2 pages is appropriate. Provide more details about your work history, achievements, and skills to showcase your professional growth.",
            "senior_level": "For senior-level resumes, aim for 2-3 pages. Include comprehensive details about your extensive experience, leadership roles, significant achievements, and any additional relevant information.",
        }
