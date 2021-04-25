list_1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
a = int(input("Ведите новый элемент списка:"))
list_1.append(a)
list_2 = sorted(list_1, reverse=True)
print(list_2)