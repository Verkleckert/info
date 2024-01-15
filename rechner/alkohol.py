volumenGetraenk = float(input('Aufgenommene Flüssigkeitsmenge in Liter: '))
anteilAlkohol = float(input('Alkoholgehalt des Getränks in Prozent: '))
massePerson = float(input('Körpermasse in kg: '))
geschlecht = input('Geschlecht (w/m): ')
getraenk = input('Getraenk ((B)ier;(S)tarkbier, Bier(M)ix, (C)ognac, (W)odka)')
# Verarbeitung
if geschlecht == 'w':
    reduktionsfaktor = 0.6
else:
    reduktionsfaktor = 0.7
if getraenk == 'B':
    anteilAlkohol = 5.0
elif getraenk == 'S':
    anteilAlkohol = 8.0
elif getraenk == 'M':
    anteilAlkohol = 2.5
elif getraenk == 'C':
    anteilAlkohol = 38.0
elif getraenk == 'W':
    anteilAlkohol = 42.0
masseAlkohol = 10*anteilAlkohol*volumenGetraenk*0.8
konzentrationAlkohol = masseAlkohol/(massePerson*reduktionsfaktor)
# Ausgabe
print('')
print('Die berechnete Alkoholkonzentration im Blut beträgt:')
print(konzentrationAlkohol, 'Promille')