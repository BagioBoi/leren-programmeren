#SwimmingGarden

zwembadLengte = 8
zwembadBreedte = 3
zwembadDiepte = 1.5
voorrijkosten = 0

afstand = (int(input("Hoeveel Km moet ik rijden om uw zwembad neer te zetten")))
zwembadInhoud = (zwembadLengte * zwembadBreedte * zwembadDiepte)
zwembadInhoudRound = round(zwembadInhoud, 2)
print (zwembadInhoudRound, "m3")

gegravenGrond = 25 * zwembadInhoudRound
afgevoerdGrond = 32.50 * zwembadInhoudRound

if afstand >= 50 and zwembadInhoudRound >= 20:
    voorrijkosten = 250 + (2.05 * afstand) 
elif afstand < 50 and zwembadInhoudRound >= 20:
    voorrijkosten = 250 + (2.15 * afstand)
elif afstand >= 50 and zwembadInhoudRound < 20:
    voorrijkosten = 100 + (1.15 * afstand)
elif afstand < 50 and zwembadInhoudRound < 20:
    voorrijkosten = 100 + (1.25 * afstand)
else:
    print("U heeft geen geldige afstanden gegeven")

print(f'''
Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud 36 m3)
Uitgraven:             €{gegravenGrond}
Afvoeren grond:        €{afgevoerdGrond}
Voorrijkosten:         €{voorrijkosten}
Totaal:                €{gegravenGrond + afgevoerdGrond + voorrijkosten}
''')

