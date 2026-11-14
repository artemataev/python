from datetime import date


def main():
    text = input("Дата події (РРРР-ММ-ДД): ")
    year, month, day = map(int, text.split("-"))
    event = date(year, month, day)
    today = date.today()

    if event > today:
        print("До події залишилося:", (event - today).days, "днів")
    elif event < today:
        print("Після події минуло:", (today - event).days, "днів")
    else:
        print("Подія сьогодні.")


main()
