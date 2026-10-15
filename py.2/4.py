width = int(input("Введіть ширину: "))
height = int(input("Введіть висоту: "))
kontur = input("Введіть символ контуру: ")
vnutr = input("Введіть символ внутрішньої частини: ")

if width < 3 or height < 3:
    print("Помилка! Ширина та висота мають бути не менше 3.")
else:
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print(kontur, end="")
            else:
                print(vnutr, end="")
        print()
