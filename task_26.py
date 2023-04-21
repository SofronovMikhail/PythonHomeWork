a = int(input("Число: "))
b = int(input("Степень: "))
c = a


def sum(a, b):
    if b == 1:
        return a
    return sum(a * c, b - 1)


print(sum(a, b))
