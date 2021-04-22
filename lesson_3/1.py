def my_f(s_1, s_2):
    try:
      sub = s_1 / s_2
    except ZeroDivisionError:
      return "Error!"
    print(round (sub, 3))

my_f(int(input("s_1: ")), int(input("s_2: ")))