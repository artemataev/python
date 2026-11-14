import random
import statistics


def main():
    n = int(input("N = "))

    if n <= 0:
        print("N має бути додатним.")
        return

    grades = []
    for i in range(n):
        grades.append(random.randint(1, 12))

    high_count = 0
    for grade in grades:
        if grade >= 10:
            high_count += 1

    print("Оцінки:", grades)
    print("Min:", min(grades))
    print("Max:", max(grades))
    print("Середнє:", round(statistics.mean(grades), 1))
    print("Медіана:", statistics.median(grades))
    print("Оцінок 10–12:", high_count)


main()
