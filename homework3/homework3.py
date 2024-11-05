n = []
while True:
  v = input("Введите целое число или 'end' для завершения работы программы: ")
  if v == "end":
    break

  try:
    number = int(v)
    n.append(number)
  except ValueError:
    print("Ошибка: Введите целое число или 'end' для завершения работы программы.")

print("Нечетные числа:")
for number in n:
  if number % 2 != 0:
    print(number)