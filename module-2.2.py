first = input('Введите 1 челое числа: ')
second = input('Введите 2 челое число: ')
third = input('Введите 2 челое число: ')
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif first == second and second == third and third == first:
    print(0)
else:
    print(0)
