# 1. Repetir una acción un número exacto de veces (del 1 al 5)
print("Counting from 1 to 5:")
for number in range(1, 6):
    print(number)

# 2. Acumular un total con un bucle
total_score = 0
for points in [10, 20, 30]:
    total_score = total_score + points

print("Total score accumulated:")
print(total_score)