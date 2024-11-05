n = []
even = 0
odd = 0

while True:
  v = input("Введите целое число или 'end' для завершения работы программы: ")
  if v == "end":
    break

  try:
    number = int(v)
    n.append(number)

    if number % 2 == 0:
      even+= 1
    else:
      odd += 1
  except ValueError:
    print("Ошибка! Введите целое число или 'end' для завершения работы программы.")

print("Введенные числа:", n)
print("Количество четных чисел:", even)
print("Количество нечетных чисел:", odd)