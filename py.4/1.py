
numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]

positive = []
negative = []
paired = []
multiples_3 = []

for n in numbers:
    if n > 0:
        positive.append(n)
    if n < 0:
        negative.append(n)
    if n % 2 == 0:
        paired.append(n)
    if n % 3 == 0:
        multiples_3.append(n)

print("Додатні:", positive)
print("Від'ємні:", negative)
print("Парні:", paired)
print("Кратні 3:", multiples_3)
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", round(sum(numbers) / len(numbers), 2))
