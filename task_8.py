print("Введите количество долек по диагонали: ")
n = int(input())
print("Введите количество долек по вертикали: ")
m = int(input())
print("Введите желаемое количество долек: ")
k = int(input())

if((k % n == 0 or k % m == 0) and n * m >= k):
    print(n, m, k, "yes")
else:
    print(n, m, k, "no")  
