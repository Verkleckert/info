input_type = str(input("Geben sie den Eingabetypen ein [c = Celsius | f = Fahrenheit]"))

input_temp = float(input("Bitte geben sie eine Temperatur in °C an (Kommas sind erlaubt): "))

if input_type == "c":
    temp = input_temp
elif input_type == "f":
    temp = (input_temp - 32) * (5/9)
else:
    print(input_type, "Ist kein gültiger Typ")
    exit()
    
if temp > 0:
    print("Bei", str(temp) + "°C ist es nicht gefrohren!")
else:
    print("Bei", str(temp) + "°C ist es gefrohren!")
