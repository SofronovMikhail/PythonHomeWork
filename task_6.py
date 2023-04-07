print("Введите шестизначое число: ")
Ticket = int(input())
if (Ticket // 100000 > 0 and Ticket // 100000 < 10):
    Ticket1 = Ticket // 1000
    Ticket2 = Ticket % 1000
    SumTicket1 = (Ticket1 % 10) + ((Ticket1 // 10) % 10) + (Ticket1 // 100)
    SumTicket2 = (Ticket2 % 10) + ((Ticket2 // 10) % 10) + (Ticket2 // 100)
    if (SumTicket1 == SumTicket2):
        print("Yes")
    else:
        print("No")    
else:
    print("Неправильное число")