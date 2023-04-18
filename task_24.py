from random import randint
number_bushes = int(input("Введите количество кустов: "))
number_berries = [randint(1, 10) for i in range(number_bushes)]
print(*number_berries)
sum_barries = set()
i = 0
while (i < number_bushes):
    sum_barries.add(number_berries[i - 2] + number_berries[i - 1] + number_berries[i])
    i += 1
print(max(sum_barries))
