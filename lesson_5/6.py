mydict = {}
with open("text_6.txt", encoding="utf-8") as fodj:
    for line in fodj:
        name, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == " " or "9" >= i >= "0"]).split()))
        mydict[name] = name_sum
print(f"{mydict}")