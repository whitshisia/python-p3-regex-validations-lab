import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^[a-zA-Z]+(?:[-'\s][a-zA-Z]+)*$"
name_regex = re.compile(name)

phone_number = r"^\+?[\d\s()-]{7,}$"
phone_regex = re.compile(phone_number)

email_address = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)
