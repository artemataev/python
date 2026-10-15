n=int(input())
kilkist = 0
suma = 0
naibilsha = 0
nainmensha = 9
if n == 0:
    kilkist = 1
    suma = 0
    naibilsha = 0
    nainmensha = 0
else:
    while n>0:
        a = n % 10
        kilkist += 1
        suma += a
        if a> naibilsha:
            naibilsha = a
        if a< nainmensha:
            nainmensha = a
        n=n//10
print("Кількість цифр:", kilkist)
print("Сума цифр:", suma)
print("Найбільша цифра:", naibilsha)
print("Найменша цифра:", nainmensha)
