def sum_num():
    s = 0
    while True:
        in_list = input("Введите число, `q` для выхода:").split()
        for num in in_list:
            if num == "q":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("Для выхода из программы, нажмите `q`: ")
        print(f"Сумма чисел = {s}")

print(sum_num())