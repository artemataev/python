
group1 = {'Anna', 'Ivan', 'Olha'}
group2 = {'Ivan', 'Maksym', 'Olha'}

print("Спільні:", ", ".join(sorted(group1 & group2)))
print("Тільки group1:", ", ".join(sorted(group1 - group2)))
print("Тільки group2:", ", ".join(sorted(group2 - group1)))
print("Усі:", ", ".join(sorted(group1 | group2)))
