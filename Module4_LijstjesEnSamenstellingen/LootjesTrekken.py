from random import shuffle
#LootjesTrekken
namenLijst = []
lootjes = []
namenLoop = True
while namenLoop:
    naamInput = input("Wat is de naam die je wilt invoeren ")
    if naamInput not in namenLijst:
        namenLijst.append(naamInput)
        lootjes.append(naamInput)
    else:
        print("Deze naam zit al in de lijst")
    if (len(namenLijst)) > 2:
        herhaalVraag = input("Wil je nog een naam toevoegen ").lower()
        if herhaalVraag == "nee":
            namenLoop = False

schudden = True
while schudden:
    shuffle(lootjes)
    schudden = False
    for index in range(len(lootjes)):
        if lootjes[index] == namenLijst[index]:
            schudden = True

getrokkenLootjes = {}
for index in range(len(namenLijst)):
    getrokkenLootjes.update({lootjes[index] : namenLijst[index]})
print (getrokkenLootjes)
