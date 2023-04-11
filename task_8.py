print("Введите количество долек по горизонтали: ")
n = int(input())
print("Введите количество долек по вертикали: ")
m = int(input())
print("Введите желаемое количество долек: ")
k = int(input())
if ((k % n == 0 or k % m == 0) and n * m >= k):
    print(n, m, k, "Yes")
else:
    print(n, m, k, "No")