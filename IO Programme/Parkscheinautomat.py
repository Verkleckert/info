stunden = int(input("Bitte geben sie die gestandenen Stunden ein: "))
gegebenes_geld = float(input("Bitte geben sie das gegebene Geld an: "))

parkgebuer = stunden * 0.5

if parkgebuer > 5:
    parkgebuer = 5

if gegebenes_geld < parkgebuer:
    zahlbetrag = parkgebuer - gegebenes_geld
    print("Noch zu zahlen:", str(zahlbetrag) + "€")
elif gegebenes_geld > parkgebuer:
    wechselgeld = gegebenes_geld - parkgebuer
    print("Ihr wechselgeld beträgt:", str(wechselgeld) + "€")
print("Parkgebür bezahlt")
