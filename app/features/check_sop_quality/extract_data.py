import itertools
import re

import pycountry


def extract_university_name(sop_text, nlp):
    doc = nlp(sop_text)

    # Initialize a list to store identified university names
    university_names = []

    for entity in doc.ents:
        # Check if the entity label is 'ORG' (organization/institution)
        if entity.label_ == "ORG":
            # Check if the entity text contains the word "university" (case-insensitive)
            if "university" in entity.text.lower():
                # Remove special characters using a regular expression
                cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", " ", entity.text)
                university_names.append(cleaned_text)

    return university_names


def extract_organization_names(sop_text, nlp):
    doc = nlp(sop_text)

    organization_names = []

    for entity in doc.ents:
        if entity.label_ == "ORG":
            cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", " ", entity.text)
            organization_name = cleaned_text.lower()
            organization_name = organization_name.split()
            organization_names.append(organization_name)

    organization_names = list(itertools.chain.from_iterable(organization_names))

    return organization_names


def extract_people_names(sop_text, nlp):
    doc = nlp(sop_text)

    people_names = []

    for entity in doc.ents:
        if entity.label_ == "PERSON":
            name = entity.text.lower()
            name = name.split()
            people_names.append(name)

    people_names = list(itertools.chain.from_iterable(people_names))

    return people_names


def extract_place_names(sop_text, nlp):
    doc = nlp(sop_text)

    place_names = []
    for ent in doc.ents:
        if ent.label_ == "GPE" or ent.label_ == "LOC":
            place_name = ent.text.lower()
            place_name = place_name.split()
            place_names.append(place_name)

    place_names = list(itertools.chain.from_iterable(place_names))

    return place_names


def is_valid_country_name(name):
    try:
        pycountry.countries.lookup(name)
        return True
    except LookupError:
        return False


def extract_destination_country_names(sop_text, nlp):
    doc = nlp(sop_text)

    destination_country_names = []
    for ent in doc.ents:
        if ent.label_ == "GPE":
            country_name = ent.text
            country_name = country_name.split()
            if is_valid_country_name(country_name[0]):
                destination_country_names.append(country_name)

    destination_country_names = list(
        itertools.chain.from_iterable(destination_country_names)
    )

    return destination_country_names
