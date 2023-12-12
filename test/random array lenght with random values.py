from random import randint

numbers = []
length = randint(10, 100)

for i in range(1, length + 1):
  numbers.append(randint(0, 100))
  
print(numbers)