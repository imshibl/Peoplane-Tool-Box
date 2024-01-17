def check_word_count(sop_text):
    word_count = (len(sop_text.split()),)

    message3 = """It's important to prioritize quality over quantity. Admissions committees appreciate well-crafted statements that directly address key aspects such as your academic background, research interests, career goals, and why you are interested in the specific program or university.
Always check the specific requirements of the program or university to which you are applying, as they may have explicit instructions regarding the length and content of the SOP. If no specific guidelines are provided, aim to strike a balance between providing sufficient detail and keeping your statement focused and engaging."""

    return {
        "word_count": word_count[0],
        "message1": "Most SOPs are typically one to two pages in length. Some programs may specify a page limit, so it's crucial to adhere to any guidelines provided by the institution.",
        "message2": "The word count for an SOP often ranges from 500 to 1500 words. This range allows applicants to convey their thoughts concisely while providing enough information.",
        "message3": message3,
    }
