def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def main():
    n = int(input("N = "))

    if is_prime(n):
        print("Просте число: так")
    else:
        print("Просте число: ні")

    print("Дільники:", divisors(n))
    print("Сума цифр:", digit_sum(n))


main()
