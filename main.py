from utils import fix_name, fix_age, fix_phone, fix_email

with open('input.txt', 'r', encoding='utf-8') as fin, open('output.txt', 'w', encoding='utf-8') as fout:
    for line in fin:
        parts = line.strip().split('|')
        if len(parts) != 4:
            continue
        name, age, phone, email = parts
        fixed = [
            fix_name(name),
            fix_age(age),
            fix_phone(phone),
            fix_email(email),
        ]
        fout.write('|'.join(fixed) + '\n')