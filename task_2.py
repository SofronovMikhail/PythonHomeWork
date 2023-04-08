print("Введите трехзначное число: ")
user_number = int(input())
i = 10
j = 100

if (user_number // j > 0 and user_number // j < 10):
    summa = (user_number % i) + ((user_number // i) % i) + (user_number // j)
    print(summa)
else:
    print("Не правильное число")
