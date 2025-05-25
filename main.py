import re

def fix_name(name):
    match = re.fullmatch(r"([А-ЯЁа-яё]+)\s?([А-ЯЁа-яё]+)", name.strip())
    if match:
        return f"{match.group(1).capitalize()} {match.group(2).capitalize()}"
    return ""

with open("input.txt", "r", encoding="utf-8") as fin, open("output.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        fout.write(line)
        fields = line.strip().split("|")
        if len(fields) != 4:
            fout.write("||| |\n")
            continue
        name, age, phone, email = fields