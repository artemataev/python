text1 = input()
text2 = input()

word1 = text1.replace(" ", "").lower()
word2 = text2.replace(" ", "").lower()

if sorted(word1) == sorted(word2):
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")

print("Перший рядок:", word1)
print("Другий рядок:", word2)