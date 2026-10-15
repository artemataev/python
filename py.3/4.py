text = input()
words = text.split()

if len(words) == 0:
    print("Речення порожнє.")
else:
    lengths = []

    for word in words:
        lengths.append(len(word))

    max_length = max(lengths)
    min_length = min(lengths)

    longest = []
    shortest = []
    unique = set()

    for word in words:
        if len(word) == max_length and word not in longest:
            longest.append(word)

        if len(word) == min_length and word not in shortest:
            shortest.append(word)

        unique.add(word.lower())

    print("Найдовші:", ", ".join(longest))
    print("Найкоротші:", ", ".join(shortest))
    print("Унікальних слів:", len(unique))

    old_word = input("Слово для заміни: ")
    new_word = input("Нове слово: ")

    result = text.replace(old_word, new_word)
    print("Після заміни:", result)