sum_addition = int(input("Введите сумму чисел: "))
sum_multiplication = int(input("Введите произведение чисел: "))
i = 1
j = 0
for i in range(sum_multiplication):
    for j in range(sum_multiplication):
        if (i * j == sum_multiplication):
            if (i + j == sum_addition):
                print(sum_addition, sum_multiplication, "=", i , j)
                break



