array1 = list(map(int, input("Введите первый набор\
     целых чисел через пробел: ").split()))
array2 = list(map(int, input("Введите первый набор\
     целых чисел через пробел: ").split()))
sum_array = set()
array = array1 + array2
for i in range(len(array)):
    sum_array.add(array[i])
print(*sum_array)
