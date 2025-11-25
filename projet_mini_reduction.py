verifier = input("tu peut calculu la reduction ,oui|non : ").strip().lower()
while verifier == "oui":
 try:
    prix_initial = float(input("Prix du produit (€) : "))
 except ValueError:
    print("Saisie invalide pour le prix.")
    exit(1)
 if prix_initial <= 0:
    print("le prix doit être positif")
    exit(1)    

 statut = input("Êtes-vous étudiant ? (o/n) ").strip().lower()
 try:
    fidelite = int(input("Fidélité (en années) : "))
 except ValueError:
    print("Saisie invalide pour la fidélité.")
    exit(1)
 code = input("entrez le code promo : ").strip().lower()

 reduction = 0.0
 r_statut = 0.0
 r_fidelite = 0.0
 r_code = 0.0
 r_prix_initial= 0.0
 if statut == "o":
    r_statut += prix_initial * 0.10
    
 elif statut == "n":
        r_statut += prix_initial * 0.05
 print("reduction etudiant est : ",r_statut,"€")   
 reduction += r_statut 

 if fidelite >= 5:
   r_fidelite += prix_initial * 0.15
 else:
    r_fidelite += prix_initial * 0.03
 print("reduction fidelite est : ",r_fidelite,"€")
 reduction += r_fidelite 
 if code == "promotion1":
    r_code += prix_initial * 0.10
    print("reduction code promo est : ",r_code,"€")


    reduction += r_code
 if prix_initial > 100:
     
     r_prix_initial += prix_initial * 0.05
     print("reduction de prix initial est : ",r_prix_initial,"€")
     reduction += 5.0
 elif prix_initial > 50 and  prix_initial < 100 :
   
     r_prix_initial += prix_initial * 0.03
     print("reduction de prix initial est : ",r_prix_initial,"€")
     reduction += 3.0
 elif prix_initial < 50:
     
    
     r_prix_initial += prix_initial * 0.0
     print("reduction de prix initial est : ",r_prix_initial,"€")
     reduction += 0.0

 prix_final = prix_initial - reduction
 if prix_final < 0:
   prix_final = 0.0
   
 print("Réduction totale est  :" ,reduction ,"€")
 print(f"Prix final : {prix_final:.2f} €")
print("welcome") 
