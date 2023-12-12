SMS_per_month = int(input("Geben sie die SMS aus diesem Monat an: "))
freie_SMS = 100

if SMS_per_month <= freie_SMS:
    kosten = 0
else:
    kosten = (SMS_per_month - freie_SMS) * 5.9

kosten_in_euro = kosten / 100

print("Die kosten Betragen", str(round(kosten_in_euro, 2)) + "€")




