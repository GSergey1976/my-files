from module_1_4 import number_my_string

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,12,14,15]
primes = []
not_primes = []
i=0
#for i in range(len(numbers)):
#    is_primes = True
#   if i == i//len(numbers[i]):
#       i=len(numbers)
#
 #       print('primes',[])
for i in numbers:
    if i > 1:
        is_primes=True
        for j in range(2,i):
            if i % j == 0:
                is_primes = False
                break
        if is_primes:
            primes.append(i)
        else:
            not_primes.append(i)
print("Простые числа", primes)
print("Не простые числа", is_primes)
