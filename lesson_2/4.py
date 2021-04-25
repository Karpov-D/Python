list_1 = input("Ведите строку из нескольких слов:").split()
print(list_1)
for i, el in enumerate(list_1, 1):
        print(f'{i}. {el[:10]}')