#LootjesTrekken
namenLoop = True
namenLijst = []
shuffleNamenLijst = []

while namenLoop:
    naamInput = input("Wat is de naam die je wilt invoeren ")
    namenLijst.append(naamInput)
    shuffleNamenLijst.append(naamInput)
    if naamInput not in namenLijst:
        herhaalVraag = input("Wil je nog een naam toevoegen ").lower()
        if herhaalVraag == "ja":
            namenLoop = True
        else:
            namenLijst = False
print(namenLijst)