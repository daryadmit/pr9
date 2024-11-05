import random

element = random.randint(0,10)
l = []

for a in range(element):
    if random.choice([True, False]):
        n = round(random.uniform(-20, 24), 2)
    else:
        n = random.randint(-10, 10)
    l.append(n)

b = []
for i in range(1, element):
    if l[i] > l[i - 1]:
        b.append(l[i])

print("Исходный список:", l)
print("Элементы, которые больше предыдущего:", b)