suggetions = {
    "sections": {
        "suggestion": "If you already have a section added in your resume (Experience, Education, Skills, etc.) and it is not getting detected by the analyzer, please double-check whether you are following the industry standards of section titles.",
        "example": {
            "good": [
                "Experience",
                "EXPERIENCE",
                "Professional Experience",
                "Education",
                "EDUCATION",
                "Projects",
            ],
            "bad": [
                "experience",
                "Professional experience",
                "education",
                "Education and training",
                "project",
            ],
        },
    },
    "mobile_number": {
        "suggestion": "Ensure a consistent and easily recognizable pattern for displaying your contact number. Use common formats like +91 1234567890 or +91 123 456 7890 to enhance readability.",
        "example": {
            "good": [
                "+91 1234567890",
                "+91 123 456 7890",
                "(+91) 1234567890",
            ],
            "bad": [
                "+911234567890",
                "911234567890",
                "1234567890",
                "91-1234567890",
            ],
        },
    },
    "name": {
        "suggestion": "Always place your name at the top/first of your resume, prominently and in a larger font size. This ensures that your name is the first thing employers notice, making it easier for them to remember and associate with your application.",
        "example": {
            "good": [
                "John Doe",
                "JANE SMITH",
                "Alice Johnson",
                "Milan Johnson K",
                "John Wick",
            ],
            "bad": [
                "Summary: Dedicated professional...",
                "Contact Information: 555-1234...",
                "Objective: Seeking a challenging...",
                "Roles: Engineer/Software Developer/Accountant...",
                "Line breaks: John\nWick",
            ],
        },
    },
    "email": {
        "suggestion": "Ensure a consistent and easily recognizable pattern for displaying your email address. Use common formats like user@example.com to enhance readability.",
        "example": {
            "good": [
                "user@example.com",
                "john.doe@example.co.uk",
                "contact.me@company.org",
            ],
            "bad": [
                "user@exampledotcom",
                "user@Gmail. Com",
                "contact@companydotorg",
                "any invalid-email-formats and unnecessary spaces",
            ],
        },
    },
    "extraction": {
        "suggestion": "Note that some resume/CV templates with extensive graphical elements or those created by third-party mobile apps may pose challenges in data extraction. Prioritize using clean and text-based templates for optimal parsing accuracy.",
        "example": {
            "good": [
                "Clean and text-based resume template",
                "Well-structured CV with minimal graphics",
                "Simple and professional layout",
                "Standard fonts and formatting",
            ],
            "bad": [
                "Resume with complex graphical elements",
                "CV generated by a third-party mobile app",
                "Templates with intricate background designs",
                "Resumes with non-standard fonts and formatting",
                "Overly stylized layouts",
            ],
        },
    },
    "cv_builder": {
        "suggestion": "Explore reputable online platforms to create professional resumes easily. Choose platforms that offer user-friendly interfaces, a variety of templates, and export options for different file formats.",
        "example": {
            "good": [
                "LinkedIn Resume Builder",
                "Canva",
                "Google Docs Templates",
                "NovoResume",
                "Resume Genius",
            ],
            "bad": [
                "Third party mobile apps",
                "Outdated apps/web-sites",
                "Suspicious platforms",
            ],
        },
    },
    "extraction_restriction": {
        "suggestion": "Please note that some PDF files may restrict copying of data, making it challenging to extract information. It is recommended to use PDFs that allow text copying for optimal data retrieval.",
        "example": {
            "good": [
                "PDF with selectable text and copy-friendly content",
                "Documents allowing easy text extraction",
                "Standard PDF format with accessible text",
                "Files with no copying restrictions for text",
            ],
            "bad": [
                "PDFs with restricted text copying",
                "Documents with encrypted or non-selectable text",
                "Files generated by tools limiting data extraction",
                "PDFs with extensive security measures hindering text copying",
                "Documents with non-standard text encoding or formatting",
            ],
        },
    },
}