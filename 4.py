MIN_LENGTH = 8


def has_min_length(password):
    return len(password) >= MIN_LENGTH


def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def has_special(password):
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return True
    return False


def validate_password(password):
    problems = []

    if not has_min_length(password):
        problems.append("мінімальна довжина - 8 символів")
    if not has_digit(password):
        problems.append("немає цифри")
    if not has_uppercase(password):
        problems.append("немає великої літери")
    if not has_lowercase(password):
        problems.append("немає малої літери")
    if not has_special(password):
        problems.append("немає спеціального символу")

    return len(problems) == 0, problems


def main():
    password = input("Password: ")
    ok, problems = validate_password(password)

    if ok:
        print("Пароль надійний.")
    else:
        print("Пароль не відповідає вимогам.")
        print()
        print("Не виконано:", ", ".join(problems))


main()
