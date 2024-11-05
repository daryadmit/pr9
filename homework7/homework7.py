import random

def cyclic_shift_right(data):

  if len(data) <= 1:
    return data

  last = data[-1]

  data = data[:-1]

  data.insert(0, last)

  return data

data = [random.randint(-10, 10) for _ in range(5)]

print("Исходный список:", data)

try:
  data = cyclic_shift_right(data)
  print("Сдвинутый список:", data)
except TypeError as e:
  print(f"Ошибка: {e}")