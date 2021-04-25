def int_func():
    for word in input("Введите слова через пробел в нижнем регистре:\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - Используйте нижний регистр!")


int_func()