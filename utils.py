import re

def clean_input(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text).strip().lower()
