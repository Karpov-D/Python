rus_disc = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_1.txt", "w", encoding="utf-8") as new_file:
    with open("text_2.txt", encoding="utf-8") as my_file:
        new_file.writelines([line.reaplase("One", rus_disc.get(line.split()[0])) for line in my_file])