height = int(input("Bitte geben sie ihre größe in cm an: "))
weight = int(input("Bitte geben sie ihr gewicht in kg an: "))

heightInMeter = height / 100

BMI = weight/(heightInMeter ** 2)

print("Ihr BMI beträgt:", round(BMI, 2))

if BMI < 18.5:
    print("Laut ihrem BMI sind Sie untergewichtig (BMI<18.5)")
elif BMI < 23.0 and BMI >= 18.5:
    print("Laut ihrem BMI haben Sie ein Normalgewicht (18.5<BMI<23)")
elif BMI < 27.5 and BMI >= 23.0:
    print("Laut ihrem BMI sind Sie übergewichtig (23<BMI<27.5)")
elif BMI >= 27.5:
    print("Laut ihrem BMI sind Sie stark übergewichtig (27.5<BMI)")
else:
    print("Leider ist ein Fehler aufgetreten bitte versuchen sie es erneut!")
