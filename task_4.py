print("Введите число: ")
SumCranes = int(input())
NumberGuys = 3
if (SumCranes // NumberGuys % 2 == 0):
    print(SumCranes//NumberGuys // 2, SumCranes//NumberGuys*2, SumCranes//NumberGuys // 2)
else:
    print("Нельзя определить")