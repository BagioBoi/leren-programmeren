from fruitmand import fruitmand
lengte = 0
for x in range(0, len(fruitmand)):
    nameList = len(fruitmand[x].get("name"))
    if nameList > lengte:
        lengte = nameList
for x in range(0, len(fruitmand)):
    if  lengte == len(fruitmand[x].get("name")):
        naam = fruitmand[x].get("name")
        kleur = fruitmand[x].get("color")
        gewicht = fruitmand[x].get("weight")

kleurTranslation = {
    "green" : "groene",
    "red" : "rode",
    "orange" : "oranje",
    "brown" : "bruine",
    "black" : "zwarte",
    "yellow" : "gele",
    "blue" : "blauwe",
    "purple" : "paarse",
    "pink" : "roze"
}
print(f'De "{naam}" ({lengte} letters) heeft een {kleurTranslation[kleur]} kleur en een gewicht van {gewicht / 1000} kg.')