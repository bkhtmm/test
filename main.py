import re

def find_okinawa(text):
    pattern = r'\bOkinawa\b'
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return None
