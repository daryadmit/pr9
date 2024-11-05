import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def get_user_numbers():
    user_numbers = []
    for i in range(len(ticket)):
        while True:
            try:
                number = int(input(f"Выберите число из предложенной строки {i + 1} {ticket[i]}: "))
                if number in ticket[i]:
                    user_numbers.append(number)
                    break
                else:
                    print("Ошибка! Число не входит в строку. Выберите число из предложенной строки.")
            except ValueError:
                print("Ошибка! Введите целое положительное число.")
    return user_numbers

def generate_random_numbers():
    return [random.choice(row) for row in ticket]

def main():

    user_numbers = get_user_numbers()

    random_numbers = generate_random_numbers()
    
    print("Выбранные вами числа:", user_numbers)
    print("Случайно сгенерированные числа:", random_numbers)

    matches = set(user_numbers) & set(random_numbers)
    
    if matches:
        print(f"Что совпало: {matches}")
        print(f"Количество совпадений: {len(matches)}")
    else:
        print("Совпадений нет.")

if __name__ == "__main__":
    main()