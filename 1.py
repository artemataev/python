PI = 3.14159


def circle_area(radius):
    return PI * radius ** 2


def rectangle_area(width, height):
    return width * height


def triangle_area(base, height):
    return base * height / 2


def main():
    print("Оберіть фігуру:")
    print("1 - круг")
    print("2 - прямокутник")
    print("3 - трикутник")
    choice = input("Фігура: ")

    if choice == "1" or choice == "круг":
        radius = float(input("Радіус: "))
        print("Площа круга: %g" % circle_area(radius))
    elif choice == "2" or choice == "прямокутник":
        width = float(input("Ширина: "))
        height = float(input("Висота: "))
        print("Площа прямокутника: %g" % rectangle_area(width, height))
    elif choice == "3" or choice == "трикутник":
        base = float(input("Основа: "))
        height = float(input("Висота: "))
        print("Площа трикутника: %g" % triangle_area(base, height))
    else:
        print("Невідома фігура.")


main()
