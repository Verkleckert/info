from random import randint

tries = 0

random_number = randint(1, 100)

while True:
  print("")
  input_number = int(input("Bitte geben sie ihre geratene Zahl ein: "))
  if input_number == random_number:
    tries += 1
    print("Sie haben die Zahlt erraten. Glückwunch!!!")
    print(f"Sie haben {tries} benötigt!")
    break
  elif input_number < random_number:
    tries += 1
    print("Die Ziehlzahl ist größer als ihre geratene Zahl")
  elif input_number > random_number:
    tries += 1
    print("Die Ziehlzahl ist kleiner als ihre geratene Zahl")
  else:
    print("Ein fehler ist aufgetreten")