counter = 1
quantity = 0

max_number = int(input("Geben sie den maximalwert an: "))

while counter <= max_number:
    if (counter % 13) == 0: 
        print(counter)
        quantity += 1
    counter += 1
print(f"Insgesamt gibt es von 0 bis {max_number} gesamt {quantity} Zahlen die durch 13 teilbar sind")
    
