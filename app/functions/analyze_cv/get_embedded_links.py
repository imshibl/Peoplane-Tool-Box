import io
from urllib.parse import urlparse

import PyPDF2


def categorize_links(links):
    categorized_links = {"LinkedIn": [], "GitHub": [], "Youtube": [], "" "Other": []}

    for link in links:
        parsed_url = urlparse(link)
        domain = parsed_url.netloc.lower()

        if "linkedin" in domain:
            categorized_links["LinkedIn"].append(link)
        elif "github" in domain:
            categorized_links["GitHub"].append(link)
        elif "youtube" in domain:
            categorized_links["Youtube"].append(link)
        else:
            categorized_links["Other"].append(link)

    return categorized_links


def extract_embedded_links(content):
    # text = ""
    links = []

    try:
        with io.BytesIO(content) as fh:
            pdf_reader = PyPDF2.PdfReader(fh)

            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                # text += page.extract_text()

                # Extract links
                for annotation in page["/Annots"]:
                    link_object = annotation.get_object()
                    if "/A" in link_object:
                        link = link_object["/A"]
                        if "/URI" in link and link["/URI"]:
                            link_text = link.get("/URI")
                            links.append(link_text)

    except Exception as e:
        print(f"Error opening PDF with PyPDF2: {e}")
        return categorize_links(links)

    categorized_links = categorize_links(links)
    # print(text)
    return categorized_links
