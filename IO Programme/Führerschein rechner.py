input_age = int(input("Wie alt sind sie? "))

if input_age == 17:
    print("Sie dürfen Begleitetes Fahren machen! Aber natürlich nur mir Eltern.")
elif input_age >= 18:
    print("Sie dürfen Auto Fahren! Aber seien sie vorsichtig ;)")
elif input_age <= 16:
    until_bf = 17 - input_age
    until_normal = 18 - input_age
    print("Sie dürfen leider noch nicht Auto fahren")
    print("Sie dürfen in", until_bf, "Jahren begleitet Fahren")
    print("Sie dürfen in", until_normal, "Jahren alleine Fahren")
else:
    print("Bitte geben sie einen gültigen Wert ein!")
