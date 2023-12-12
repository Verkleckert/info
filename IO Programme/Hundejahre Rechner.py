import time

# Input
dog_age = int(input("Bitte geben sie das Alter ihres Hundes an: "))

# Check data
if dog_age <= 0:
    print("Bitte geben sie einen Validen wert an!")
elif dog_age == 1:
    print("Ihr Hund ist 14 Jahre alt")
elif dog_age > 1:
    dog_age_as_human = 22 + 5 * (dog_age - 2)
    print("Ihr Hund ist", dog_age_as_human, "Jahre alt")

