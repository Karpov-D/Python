lis = []
n = int(input('Введите колличество элементов в списке:'))
print("Введите элементы списка:")
for i in range(0, n):
    ele = input()
    lis.append(ele)
for i in range(1, len(lis), 2):
    lis[i - 1], lis[i] = lis[i], lis[i - 1]
    print(lis)