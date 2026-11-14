import math


def main():
    radius = float(input("Радіус: "))

    legs = input("Катети: ").replace(",", " ").split()
    a = float(legs[0])
    b = float(legs[1])

    items = int(input("Предметів: "))
    per_pack = int(input("В упаковці: "))

    area = math.pi * radius ** 2
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    packs = math.ceil(items / per_pack)

    print("Площа круга:", round(area, 2))
    print("Гіпотенуза:", round(hypotenuse, 2))
    print("Потрібно упаковок:", packs)


main()
