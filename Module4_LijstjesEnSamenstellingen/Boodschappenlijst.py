keuze = True
boodschappenlijst = {}


while keuze:
    product = input("Wat wilt u toevoegen aan de boodschappenlijst").lower().strip()
    while True:
        try:
            aantalproduct = int(input("Hoeveel van dit product wilt u toevoegen"))
            break
        except:
            print("Dat is geen geldig nummer")
    
    if product in boodschappenlijst:
        boodschappenlijst[product] += aantalproduct
    else:
        boodschappenlijst.update({product : aantalproduct})

    while True:
        herhaling = input("Wil je nog een product toevoegen?")
        if herhaling in ["ja","j","y","yes"]:
            keuze = True
            break
        else:
            keuze = False
            break
print(boodschappenlijst)




    