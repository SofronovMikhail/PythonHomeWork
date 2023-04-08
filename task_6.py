print("Введите шестизначое число: ")
ticket = int(input())
if (ticket // 100000 > 0 and ticket // 100000 < 10):
    ticket_1 = ticket // 1000
    ticket_2 = ticket % 1000
    sum_ticket1 = (ticket_1 % 10) + ((ticket_1 // 10) % 10) + (ticket_1 // 100)
    sum_ticket2 = (ticket_2 % 10) + ((ticket_2 // 10) % 10) + (ticket_2 // 100)
    if (sum_ticket1 == sum_ticket2):
        print("Yes")
    else:
        print("No")
else:
    print("Неправильное число")
