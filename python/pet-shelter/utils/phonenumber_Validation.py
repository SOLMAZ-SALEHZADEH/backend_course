import re

def phonenumber_validation(phone):
    pattern = r"^09\d{9}$"
    if re.match(pattern, phone):
        return True
    else:
        return False






