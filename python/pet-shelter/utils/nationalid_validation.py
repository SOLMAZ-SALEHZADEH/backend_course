import re

def nationalid_validation(national_id):
    if not re.fullmatch(r"\d{10}", national_id):
        return False

    digits = [int(x) for x in national_id]

    total = sum(
        digits[i] * (10 - i)
        for i in range(9)
    )

    remainder = total % 11

    check_digit = remainder if remainder < 2 else 11 - remainder

    return digits[9] == check_digit