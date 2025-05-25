from utils import fix_name, fix_age, fix_phone, fix_email

def test_fix_name():
    assert fix_name("ИванИванов") == "Иван Иванов"
    assert fix_name("Иван Иванов") == "Иван Иванов"
    assert fix_name("иваниванов") == ""

def test_fix_age():
    assert fix_age("27") == "27"
    assert fix_age("150") == ""
    assert fix_age("abc") == ""

def test_fix_phone():
    assert fix_phone("+79990001111") == "+7 (999) 000-11-11"
    assert fix_phone("8 (999) 000-11-11") == "+7 (999) 000-11-11"
    assert fix_phone("123") == ""

def test_fix_email():
    assert fix_email("example@yandex.ru") == "example@yandex.ru"
    assert fix_email("example@@yandex..ru") == ""
    assert fix_email("exa mple@yandex.ru") == "example@yandex.ru"
