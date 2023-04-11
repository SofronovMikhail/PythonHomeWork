print("Введите число: ")
sum_cranes = int(input())
number_guys = 3
if (sum_cranes / number_guys % 2 == 0):
    print(sum_cranes // number_guys // 2, sum_cranes // number_guys * 2,
          sum_cranes // number_guys // 2)
else:
    print("Нельзя определить")
