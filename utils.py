import re

def fix_name(name: str) -> str:
    match = re.match(r'^([А-ЯЁ][а-яё]+)([А-ЯЁ][а-яё]+)$', name)
    if match:
        return f"{match.group(1)} {match.group(2)}"
    if re.match(r'^[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$', name):
        return name
    return ''

def fix_age(age: str) -> str:
    if age.isdigit() and 0 < int(age) < 120:
        return age
    return ''

def fix_phone(phone: str) -> str:
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 11 and digits.startswith('8'):
        digits = '7' + digits[1:]
    if len(digits) == 11 and digits.startswith('7'):
        return f'+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:]}'
    return ''

def fix_email(email: str) -> str:
    email = re.sub(r'\s+', '', email)
    email = re.sub(r'\.{2,}', '.', email)
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return email
    return ''
