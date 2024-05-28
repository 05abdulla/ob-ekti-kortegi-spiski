immutable_var = tuple([37, 1986, "Abdulla", 'Dagestan'])
print(immutable_var)
#tuple[0] = 40 # в переменной immutable_var, элементы кортежа в данном случае не изменяемые, так как кортежи не изменяемы
#print(tuple)

mutable_list = [2, 2, 1, 'laptop', 'mouse', 'headphones']
print(mutable_list)
mutable_list[3] = 'smartphone'
mutable_list[0] = 1
print(mutable_list)