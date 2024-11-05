import random

def swap_min_max(data):

  if len(data) <= 1:
    return data

  for element in data:
    if not isinstance(element, (int, float)):
      raise TypeError("Список должен содержать только числа.")

  mini = data.index(min(data))
  maxi = data.index(max(data))

  data[mini], data[maxi] = data[maxi], data[mini]

  return data

data = [random.randint(-10, 10) for _ in range(5)]

print("Исходный список:", data)

try:
  data = swap_min_max(data)
  print("Список после изменения:", data)
except TypeError as e:
  print(f"Ошибка: {e}")