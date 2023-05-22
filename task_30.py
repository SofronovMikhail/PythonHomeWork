a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
length = int(input("Введите колличество элементов: "))
count = list()

def arithmetic_progression(a1, length):
    count.append(d)
    for i in range(1,length):
        a1 = a1 + d
        count.append(a1)
    return count


def arithmetic_progression(a1, length):
    if length == 1:
        return count   
    a1 += d
    arithmetic_progression(a1, length - 1)
    count.append(a1)
    return count


print(arithmetic_progression(a1, length)) 

   