def my_f(s_1, s_2, s_3):
    my_list = [s_1, s_2, s_3]
    sub = s_1 + s_2 + s_3 - min(my_list)
    print(sub)


my_f (int(input("s_1: ")), int(input("s_2: ")), int(input("s_3: ")))