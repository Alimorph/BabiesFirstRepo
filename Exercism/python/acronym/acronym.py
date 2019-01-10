import re

def abbreviate(words):
    acronym = ""
    for word in re.findall(r"[\w']+", words):
        acronym = acronym + word[0]
    return acronym.upper()