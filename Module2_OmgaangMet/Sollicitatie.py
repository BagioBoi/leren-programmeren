praktijk_ervaring = input('''Heeft u ervaring in dieren-dressuur, jongleren of acrobatiek
1 = dieren-dressuur
2 = jongleren
3 = acrobatiek
4 = geen ervaring 
''')
dieren_dressuur = 0
jongleren = 0
acrobatiek = 0
ervaring = 0

if praktijk_ervaring == '1':
    dieren_dressuur = int(input("Hoeveel jaar ervaring heb je in dieren-dressuur?: " ))

elif praktijk_ervaring == '2':
    jongleren = int(input("Hoeveel jaar ervaring heb je in jongleren?: " ))

elif praktijk_ervaring == '3':
    acrobatiek = int(input("Hoeveel jaar ervaring heb je in acrobatiek?: " ))

else:
    pass    

if (dieren_dressuur > 4) or (jongleren > 5) or (acrobatiek > 3):
    dieren_dressuur = True
    jongleren = True
    acrobatiek = True
    ervaring = dieren_dressuur or jongleren or acrobatiek
else:
    dieren_dressuur = False
    jongleren = False
    acrobatiek = False

mbo = False
mbo_antwoord = input("Heeft u een MBO diploma of hoger niveau? ja/nee: ")
if mbo_antwoord == "ja":
    niveau = int(input("Welk MBO niveau heeft u behaald: "))
    if niveau > 4:
        mbo = True

antwoord_vrachtwagen = input("Bent u in bezit van een vrachtwagen rijbewijs? ja/nee: ")
vrachtwagen = antwoord_vrachtwagen == "ja"

linkshandig = input("Bent u linkshandig? ja/nee: ")
#Deze vraag gaat niks mee gedaan worden

antwoord_hoed = input("Bent u in bezit van een hoed? ja/nee: ")
hoed = antwoord_hoed == "ja"

gender = False
gender = input("Bent u een man of vrouw? man/vrouw: ")
if gender == "man":
    snor = input("Heeft u dan een snor? ja/nee: ")
    if snor == "ja":
        snor_breedte = int(input("Wat is de breedte van uw snor in cm?: "))
        if snor_breedte > 10:
            gender = True

elif gender == "vrouw":
    rood_krulhaar = input("Heeft u rood krulhaar? ja/nee: ")
    if rood_krulhaar == "ja":
        lengte_haar = int(input("hoelang is uw haar in cm?: "))
        if lengte_haar > 20:
            gender = True

else:
    pass

lengte = int(input("Hoelang bent u in cm?: "))
if lengte > 150:
    lengte = True

huisdier = input("Heeft u huisdieren? ja/nee: ")
if huisdier == "ja":
    aantal_huisdieren = input("Hoeveel huisdieren heeft u dan: ")
#weer een vraag waar niks gedaan mee wordt

gewicht = int(input("Hoeveel weegt u in kg?: "))
if gewicht < 90:
    gewicht = True

muizen_vanger = input("Heeft u het certificaat muizenvanger? ja/nee: ")
#vraag waar niks gedaan mee wordt

antwoord_certificaat_ogp = input("Heeft u het certificaar overleven met gevaarlijk personeel? ja/nee: ")
certificaat_ogp = antwoord_certificaat_ogp == "ja"

if (ervaring and mbo and vrachtwagen and hoed and gender and lengte and huisdier and gewicht and certificaat_ogp == True):
    print("Je bent gekwalificeerd voor de baan. Stuur zo snel mogelijk je CV op.")
else: 
    print("je bent niet gekwalificeerd voor de baan.")