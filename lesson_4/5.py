from functools import reduce


my_list = [num for num in range(100, 1001, 2)]
s_1 = reduce(lambda x,y: x * y, my_list)
print(my_list)
print(s_1)