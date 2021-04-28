with open("text_1.txt", "w", encoding="utf-8") as f:
    while True:
        line = input("Введите данные или пустую строку для завершения:")
        if not line:
            break
        print(line, file=f)