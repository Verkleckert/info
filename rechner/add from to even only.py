start = int(input("Bitte geben sie eine Startzahl ein: "))
end = int(input("Bitte geben sie eine Endzahl ein: "))

sum = 0

for index in range(start, end + 1):
  if (index % 2) == 0:
    sum += index
  
print(f"Die summe aller geraden zahlen zwichen {start} und {end} ist {sum}")