input_number = int(input("Bitte geben sie eine Zahl an: "))

input_number_mod = (input_number % 2)

if input_number_mod == 1:
    odd_or_even = "ungerade"
elif input_number_mod == 0:
    odd_or_even = "gerade"
    
if input_number == 10:
    print("Ihre zahl ist 10 und sie ist", odd_or_even + ".")
elif input_number < 10:
    print("Ihre zahl ist kleiner als 10 und sie ist", odd_or_even + ".")
elif input_number > 10:
    print("Ihre zahl ist größer als 10 und sie ist", odd_or_even +".")
