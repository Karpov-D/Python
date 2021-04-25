from random import randint

my_list = [randint(1, 10) for _ in range(20)]
new_list = [num for num in my_list if my_list.count(num) == 1]

print(my_list)
print(new_list)