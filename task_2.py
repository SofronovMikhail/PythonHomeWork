print("Введите трехзначное число: ")
UserNumber = int(input())
i = 10
j =100

if(UserNumber // j > 0 and UserNumber // j < 10):
    Summa = (UserNumber %i) + ((UserNumber // i) % i) + (UserNumber // j)
    print(Summa)
else:
    print("Не правильное число")        