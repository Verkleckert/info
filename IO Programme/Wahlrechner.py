demokraten = int(input("Stimmen der Demokraten:"))
republikaner = int(input("Stimmen der Republikaner:"))

gesamt = republikaner + demokraten

prozent_demokraten = (demokraten / gesamt)*100
prozent_republikaner = (republikaner / gesamt)*100

print(f"Die Demokraten haben: {prozent_demokraten}%")
print(f"Die Republikaner haben: {prozent_republikaner}%")
