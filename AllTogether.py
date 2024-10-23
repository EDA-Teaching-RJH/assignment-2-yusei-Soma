### Part Four -- your code goes here. 
import random
x = [random.randint(1, 100) for _ in range(10)]
print("first List:", x)
y = 0
while y < len(x):
    if x[y] % 2 == 0:
        x.pop(y)
    else:
        y += 1

print("Odd Numbers:",x)
