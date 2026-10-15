x, y = map(float, input("Введіть координати точки через пробіл (x y): ").split())

if x > 0 and y > 0:
    print("Точка належить I чверті")
elif x < 0 and y > 0:
    print("Точка належить II чверті")
elif x < 0 and y < 0:
    print("Точка належить III чверті")
elif x > 0 and y < 0:
    print("Точка належить IV чверті")
else:
    print("Точка лежить на осі координат")
