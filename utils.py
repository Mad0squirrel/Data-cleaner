import re

def fix_name(name):
    match = re.fullmatch(r"([А-ЯЁа-яё]+)\s?([А-ЯЁа-яё]+)", name.strip())
    if match:
        return f"{match.group(1).capitalize()} {match.group(2).capitalize()}"
    return ""

def fix_age(age):
    try:
        age_int = int(re.sub(r"[^\d]", "", age))
        if 0 < age_int < 120:
            return str(age_int)
    except:
        pass
    return ""

def fix_phone(phone):
    digits = re.sub(r"\D", "", phone)
    if len(digits) == 11 and digits.startswith("8"):
        digits = "7" + digits[1:]
    if len(digits) == 11 and digits.startswith("7"):
        return f"+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:]}"
    return ""

def fix_email(email):
    email = email.strip()
    if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
        return email
    return ""
