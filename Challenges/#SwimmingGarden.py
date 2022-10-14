#SwimmingGarden

zwembadLengte = float(input("Wat is de lengte van het zwembad in meters: "))
zwembadBreedte = float(input("Wat is de breedte van het zwembad in meters: "))
zwembadDiepte = float(input("Wat is de diepte van het zwembad in meters: "))
afstand = int(input("Hoeveel Km moet ik rijden om uw zwembad neer te zetten"))
tegelKeuze = input("Welke kleur tegel wilt u kiezen. standaard, rood of keuze.").lower()
zwembadInhoud = (zwembadLengte * zwembadBreedte * zwembadDiepte)
zwembadVierkanteMeter = (zwembadLengte * zwembadBreedte)
zwembadInhoudRound = round(zwembadInhoud, 2)
tegelAantal = (zwembadLengte * zwembadDiepte) * 2 + (zwembadBreedte * zwembadDiepte) * 2 + (zwembadBreedte * zwembadLengte)
gegravenGrond = 25 * zwembadInhoudRound
afgevoerdGrond = 32.50 * zwembadInhoudRound

if tegelKeuze == "standaard" and zwembadInhoudRound < 20:
    tegelMeerPrijs = 250
elif tegelKeuze == "standaard" and zwembadInhoudRound >= 20:
    tegelMeerPrijs = 200
elif tegelKeuze == "rood" and zwembadInhoudRound < 20:
    tegelMeerPrijs = 250 + 25
elif tegelKeuze == "rood" and zwembadInhoudRound >= 20:
    tegelMeerPrijs = 200 + 20
elif tegelKeuze == "keuze" and zwembadInhoudRound < 20:
    tegelMeerPrijs = 250 + 100
elif tegelKeuze == "keuze" and zwembadInhoudRound >= 20:
    tegelMeerPrijs = 200 + 125
tegelEindPrijs = tegelAantal * tegelMeerPrijs
if afstand >= 50 and zwembadInhoudRound >= 20:
    voorrijkosten = 250 + (2.05 * afstand) 
elif afstand < 50 and zwembadInhoudRound >= 20:
    voorrijkosten = 250 + (2.15 * afstand)
elif afstand >= 50 and zwembadInhoudRound < 20:
    voorrijkosten = 100 + (1.15 * afstand)
elif afstand < 50 and zwembadInhoudRound < 20:
    voorrijkosten = 100 + (1.25 * afstand)
else:
    print("U heeft geen geldige gegevens gegeven")

print(f'''
Offerte voor een zwembad van {zwembadLengte} bij {zwembadBreedte} bij {zwembadDiepte} meter (inhoud {zwembadInhoudRound} m3)
Uitgraven:                       €{round(gegravenGrond, 2)}
Afvoeren grond:                  €{round(afgevoerdGrond, 2)}
Voorrijkosten:                   €{round(voorrijkosten, 2)}
Beton + tegel ({tegelAantal} m2)          €{round(tegelEindPrijs, 2)}
Totaal:                          €{gegravenGrond + afgevoerdGrond + voorrijkosten + tegelEindPrijs}
''')

