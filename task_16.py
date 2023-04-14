array = list(map(int, input("Введите элементы массива: ").split()))
user_num = int(input("Введите искомое число: "))
if(array.count(user_num)):
    print(array.count(user_num))
else:
    print("Такого числа нет")