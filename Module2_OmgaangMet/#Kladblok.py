#Kladblok
# woord = input("Voer hier een woord in").lower()
# woord2 = ""
# for i in woord:
#     woord2 = woord2 + i + i
# print (woord2)
zwembadLengte = float(input("Wat is de lengte van het zwembad in meters: "))
zwembadBreedte = float(input("Wat is de breedte van het zwembad in meters: "))
zwembadDiepte = float(input("Wat is de diepte van het zwembad in meters: "))
afstand = int(input("Hoeveel Km moet ik rijden om uw zwembad neer te zetten"))
tegelKeuze = input("Welke kleur tegel wilt u kiezen. standaard, rood of keuze.").lower()
zwembadInhoud = (zwembadLengte * zwembadBreedte * zwembadDiepte)
zwembadVierkanteMeter = (zwembadLengte * zwembadBreedte)
zwembadInhoudRound = round(zwembadInhoud, 2)
tegelAantal = (zwembadLengte * zwembadDiepte) * 2 + (zwembadBreedte * zwembadDiepte) * 2 + (zwembadBreedte + zwembadLengte)

tegelWand1 = (zwembadLengte * zwembadDiepte) * 2
tegelWand2 = (zwembadBreedte * zwembadDiepte) * 2
tegelWand3 = (zwembadBreedte * zwembadLengte)

print(tegelWand1)
print(tegelWand2)
print(tegelWand3)
