import re


def check_date(text):

    
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"

    result = re.search(pattern, text)

    if result:
        return True
    else:
        return False


print(check_date("My birthday is on 25/06/2024"))
print(check_date("The meeting is tomorrow"))