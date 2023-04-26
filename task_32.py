from random import randint
length = int(input("Количество элементов: "))
array = [randint(1 , 10) for i in range(length)]
print(array)
min = int(input("Минмальное значение: "))
max = int(input("Максимальное значение: "))
sort_array = list()

def output():
    for i in range(length - 1):
        if(array[i] >= min and array[i] <= max):
            sort_array.append(i)
    return sort_array


print(output())