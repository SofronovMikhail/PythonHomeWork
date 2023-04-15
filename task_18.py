array = list(map(int, input("Введите элементы массива: ").split()))
user_num = int(input("Введите искомое число: "))
i = 0
index = 0
array_end = list()
while (i < len(array)):
    array_end.append(array[i] - user_num)
    if (array_end[i] < 0):
        array_end[i] *= -1
    i += 1
min = min(array_end)
for i in range(len(array_end)):
    if (min == array_end[i]):
        index = i
        break
print(f"Самое ближнее минимальное число: {array[index]}")
