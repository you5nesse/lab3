age = 22
permis = True
casier_vierge = False

peut_conduire = (age >= 18) and permis
print(peut_conduire)

peut_louer_voiture = (age >= 21) or (permis and casier_vierge)
print(peut_louer_voiture)

sanction = not casier_vierge
print(sanction)
