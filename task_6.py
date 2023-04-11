print("Введите шестизначое число: ")
ticket = int(input())
if (ticket // 100000 > 0 and ticket // 100000 < 10):
    ticket1 = ticket // 1000
    ticket2 = ticket % 1000
    sum_ticket1 = (ticket1 % 10) + ((ticket1 // 10) % 10) + (ticket1 // 100)
    sum_ticket2 = (ticket2 % 10) + ((ticket2 // 10) % 10) + (ticket2 // 100)
    if (sum_ticket1 == sum_ticket2):
        print("Yes")
    else:
        print("No")
else:
    print("Неправильное число")
