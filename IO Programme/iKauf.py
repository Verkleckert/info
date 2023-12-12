auftragswert = round(float(input("Bitte geben sie Ihren Auftragswert in Euro an [Nur Zahlen mit oder ohne Komma]")),2)
versandpauschale = 3.5

if auftragswert < 100.0:
    gesamtbetrag = auftragswert + versandpauschale
else:
    rabatt = auftragswert * 0.02
    gesamtbetrag = auftragswert - rabatt

print("Ihr Gesamtbetrag ist:", gesamtbetrag)






