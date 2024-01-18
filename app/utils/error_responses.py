class APIErrorResponses:
    notAPremiumUserErrorResponse = {
        "error": "Not a premium user",
        "message": "Sorry, this is a premium feature. Please upgrade to premium package to use this feature",
    }

    contentIsShortOrEmptyErrorResponse = {
        "error": "SOP is empty or is too short",
        "message": "Please provide a valid Statement of Purpose (SOP) to check quality",
    }

    underMaintenanceErrorResponse = {
        "error": "Service temporarily unavailable",
        "message": "We are currently working on some updates. It may take some time. We appreciate your patience.",
    }

    userNotFoundErrorResponse = {
        "error": "User not found",
        "message": "User does not exist",
    }

    noPermissionErrorResponse = {
        "error": "No permission",
        "message": "User does not have permission to perform this action",
    }

    fileNotSelectedErrorResponse = {
        "error": "File not selected",
        "message": "Please select a PDF file to upload",
    }

    notAPdfFileErrorResponse = {
        "error": "Incorrect File Format",
        "message": "Invalid file format. Please upload a PDF file format of your resume. We recommend always creating resumes in PDF format for optimal compatibility and presentation.",
    }
