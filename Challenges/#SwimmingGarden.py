#SwimmingGarden

zwembadLengte = 8
zwembadBreedte = 3
zwembadDiepte = 1.5

zwembadInhoud = (zwembadLengte * zwembadBreedte * zwembadDiepte)
zwembadInhoudRound = round(zwembadInhoud, 2)
print (zwembadInhoudRound, "m3")

gegravenGrond = 25 * zwembadInhoudRound
afgevoerdGrond = 32.50 * zwembadInhoudRound

print(f'''
Uitgraven:             €{gegravenGrond}
Afvoeren grond:        €{afgevoerdGrond}
Totaal:                €{gegravenGrond + afgevoerdGrond}
''')