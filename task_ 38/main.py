import functions as func


while True:
    print('1. вывод, 2. добавление, 3. поиск')
    mode = int(input())
    if mode == 1:
        func.show_data()
    elif mode == 2:
        func.add_data()
    elif mode == 3:
        func.find_data()
    else:
        break