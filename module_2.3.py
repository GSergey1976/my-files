my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # исходный список
nul = 0   # задаём счетчик
print('Список', my_list )

while nul < len(my_list):
    num = my_list[nul]    # задаём число из списка
    nul = nul + 1   # запускаем счетчик
    if num == 0:
        continue    # пропускаем 0
    elif num < 0:
        break   # остановка при отридцательном числе
    elif nul == len(my_list):
        print(num)
    else:
        print(num)
print('Список закончился')