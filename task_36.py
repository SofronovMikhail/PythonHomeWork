str = "house=дом car=машина men=человек tree=дерево"
str2 = str.split()
tp = tuple(map(lambda x:  (x[0], x[1]), map(lambda x: x.split("="), str2)))
print(tp)