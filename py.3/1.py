text = input()

symbols = len(text)
letters = 0
digits = 0
spaces = 0
vowels = 0

for char in text:
    if char.isalpha():
        letters += 1
    if char.isdigit():
        digits += 1
    if char == " ":
        spaces += 1
    if char.lower() in "aeiou":
        vowels += 1

words = len(text.split())

print("Символів:", symbols)
print("Літер:", letters)
print("Цифр:", digits)
print("Пробілів:", spaces)
print("Голосних:", vowels)
print("Слів:", words)