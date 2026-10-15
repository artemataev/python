text = input()
words = text.split()

if len(words) != 3:
    print("Помилка: потрібно ввести прізвище, ім'я та по батькові")
else:
    surname = words[0].capitalize()
    name = words[1].capitalize()
    patronymic = words[2].capitalize()

    print(surname, name[0] + "." + patronymic[0] + ".")