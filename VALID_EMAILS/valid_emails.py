import re
from typing import List

# Pre-compile the regex pattern for better performance
valid_email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")


def valid_emails(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""
    # Use a list comprehension for better performance and readability
    return [email for email in strings if valid_email_regex.match(email)]
