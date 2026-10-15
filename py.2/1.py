n=int(input())
suma = 0
kilkisty = 0
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        suma += i
        kilkisty += 1

print("кількість", kilkisty)
print("сума", suma)

if kilkisty > 0:
    ser = suma / kilkisty
    print("середнє", ser)
