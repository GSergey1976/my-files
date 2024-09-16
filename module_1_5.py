immutable_var = (1, 2, 3, True, "apple")
print('Immutable tuple:', immutable_var)
# immutable_var[1]=5 кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 'a', 'b']
mutable_list = mutable_list = [1, 2, 'a', 'b'] + ['apple']
print('Mutable_list:', mutable_list)
