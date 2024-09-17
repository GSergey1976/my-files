my_dick = {'Sergey': 1976, 'Aleksandr': 1991, 'Denis': 1985}
print(my_dick)
print('Existing value:', my_dick['Denis'])
print('Not existing value:', my_dick.get('Mixail'))
my_dick.update({'Kira': 2001, 'Dina': 1999})
print('Deleted value:', my_dick['Dina'])
del my_dick['Dina']
print('Modified dictionary:', my_dick)

my_set = {1, 2, 3, 'apple', 234.15, 1, 3, 3, 4}
print('Set:', my_set)
my_set.update({(5, 6)})
print('Set 2:', my_set)
my_set.discard('apple')
print('Modified set:', my_set)
