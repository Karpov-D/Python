from sys import argv

name, s_1, s_2, = argv
s_1 = int(s_1)
s_2 = int(s_2)
s_3 = s_1 * s_2 * 0.2

print("Выработка в часах: ", s_1)
print("Ставка в час: ", s_2)
print("Премия: ", s_3)
print("Зарплата: ", float((s_1 * s_2)+s_3))