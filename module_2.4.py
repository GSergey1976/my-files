numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
i = 0
for i in numbers:
    if i > 1:
        is_primes = True
        for j in range(2, i):
            if i % j == 0:
                is_primes = False
                continue
        if is_primes:
            primes.append(i)
        else:
            not_primes.append(i)
is_primes = True
print("Простые числа", primes)
print("Не простые числа", not_primes)
