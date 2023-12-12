input_number = int(input("Geben sie eine Endwert an: "))
teiler, prime = [], False

for i in range(1, input_number +1):
  if (input_number % i) == 0 :
    teiler.append(i)
    
if len(teiler) == 2:
  prime = True

print(f"Die gegebene Zahl {input_number} ist {('eine' if prime else 'kein')} Primzahl.")
print("Ihre möglichen Teiler sind die folgenden:")

for print_var in teiler:
  print(print_var)

