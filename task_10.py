count_money = int(input("Введите колличество монет: "))
i = 1
count_false = 0
count_true = 0
while count_money >= i:
    side = int(input())
    if (side == 0):
        count_false += 1
    if (side == 1):
        count_true += 1
    i += 1
if (count_true > count_false):
    print(count_false)
else:
    print(count_true)
