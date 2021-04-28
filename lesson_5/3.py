def task_3():
    wages = {}
    try:
        with open("task_3.txt", "r", encoding="utf-8") as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print("Меньше 20000 получают:")
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f"Средяя зарплата равна {sum(wages.values()) / len(wages)}")
    except IOError:
        print("Ошибка!")