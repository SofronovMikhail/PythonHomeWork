user_number = int(input("Введите число: "))
constanta = 2
for i in range(user_number):
    multiplication = constanta ** i
    if (multiplication >= user_number):
        break
    print(multiplication)
    