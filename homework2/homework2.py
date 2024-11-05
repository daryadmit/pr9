def get_squares(a, b):
    s = int(a) + 1 if a < b else int(b) + 1
    f = int(b) if a < b else int(a)

    squares = [i ** 2 for i in range(s, f)]
    return squares

while True:
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        break  
    except ValueError:
        print("Некорректный ввод данных!")

squares_list = get_squares(a, b)
print("Список квадратов целых чисел между a и b:", squares_list)