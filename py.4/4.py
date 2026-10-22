
group_info = ('10-IT', '2026/2027')

journal = {
    "Anna": [10, 11, 12, 9, 10],
    "Ivan": [8, 9, 10, 11, 9]
}

print("Група:", group_info[0], "—", group_info[1])

name = input("Введіть ім'я нового учня: ")
grades = list(map(int, input("Введіть 5 оцінок через пробіл: ").split()))

if len(grades) == 5 and all(1 <= g <= 12 for g in grades):
    journal[name] = grades
else:
    print("Помилка! Потрібно ввести 5 оцінок від 1 до 12.")

print("\nЖурнал групи:")

averages = {}

for name, grades in journal.items():
    average = sum(grades) / 5
    averages[name] = average
    print(name, ":", *grades, "— середній бал:", round(average, 1))

print("\nРейтинг учнів:")

rating = sorted(averages.items(), key=lambda item: item[1], reverse=True)

for name, average in rating:
    print(name, "—", round(average, 1))

best = max(averages, key=averages.get)

print("\nНайкращий результат:", best, "—", round(averages[best], 1))
