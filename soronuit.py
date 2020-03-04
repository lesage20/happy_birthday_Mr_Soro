
def prix_supplement(prix_heure_unitaire, heures_totale):
#variable
    heures_suppl = 0
    prix_heures_total = prix_heure_unitaire * heures_totale
    prix_heures_suppl = 0

    heures_suppl1 = heures_totale - 39
    prix_heures_suppl1 = heures_suppl1 * prix_heure_unitaire + ((heures_suppl1*prix_heure_unitaire*50)/100)
    prix_heures_suppl2 = 5 * prix_heure_unitaire * 1.5 + (heures_totale - 44) * prix_heure_unitaire * 1.75
    prix_heures_suppl3 = 5 * prix_heure_unitaire * 1.5 + 5 * prix_heure_unitaire * 1.75 + (heures_totale - 49) * prix_heure_unitaire *2

    if heures_totale == 39:
        
        print("Vous n'avez pas assez travailler votre salaire reste intact")
    elif 39 < heures_totale < 45 :
        
        print( f"Vous avez recu une augmentation de : {int(prix_heures_suppl1)}$" )
    elif 45 <= heures_totale < 49:
        print( f"Vous avez recu une augmentation de : {int(prix_heures_suppl2)}$" )
    elif heures_totale >= 50:
        print( f"Vous avez recu une augmentation de : {int(prix_heures_suppl3)}$" )
    else:
        heure_abs = 39 - heures_totale
        print(f"Vous avez {heure_abs} heures en absence il vous sera  reduire {heure_abs*2}$ de votre salaire.")

