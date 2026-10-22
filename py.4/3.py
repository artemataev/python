
products = {
    "milk": 48,
    "tea": 75,
    "bread": 30,
    "coffee": 120
}

name = input("Назва товару: ")
price = float(input("Ціна товару: "))
products[name] = price

search = input("Знайти товар: ")
result = products.get(search)

if result is not None:
    print(search, "—", result, "грн")
else:
    print("Товар не знайдено")

low = float(input("Мінімальна ціна: "))
high = float(input("Максимальна ціна: "))

for name, price in products.items():
    if low <= price <= high:
        print(name, "—", price, "грн")
