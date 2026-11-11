def average(grades):
    return sum(grades) / len(grades)


def minimum(grades):
    return min(grades)


def maximum(grades):
    return max(grades)


def count_above(grades, value):
    count = 0
    for grade in grades:
        if grade > value:
            count += 1
    return count


def main():
    text = input("Оцінки: ")
    text = text.replace("[", "").replace("]", "").replace(",", " ")
    grades = [int(x) for x in text.split()]
    limit = int(input("Поріг: "))

    print("Середній бал:", average(grades))
    print("Мінімальна:", minimum(grades))
    print("Максимальна:", maximum(grades))
    print("Вище %s: %s" % (limit, count_above(grades, limit)))


main()
