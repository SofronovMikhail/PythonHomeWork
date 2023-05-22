text = list(input("Введите фразу Винни-Пуха: ").split())

result = lambda x: "Парам пам-пам" if x.count(x[0]) == len(x) else "Пам парам"

print(result(list(map(lambda x: x.count("а"), text))))