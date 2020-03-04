point_depart = 100

victime_poulet, victime_chien, victime_vache, victime_ami = int(input("Combien de poulet avez vous tué: ")), int(input("Combien de chien avez vous tué: ")), int(input("Combien de vache avez vous tué: ")),int(input("Combien de ami avez vous tué: "))
amende = ((victime_poulet + victime_chien * 3 + victime_vache * 5 + victime_ami * 10)*2)

if amende > 0:    
    print(f"vous devez {abs(amende)}$ d'amende pour avoir tuer des animaux domestiques")
elif amende == 0:
    print("Vous n'etes pas amendé mais vous n'avez pas accès au permis de chasse ")





