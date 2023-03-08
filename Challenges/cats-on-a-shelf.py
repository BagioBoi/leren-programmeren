#cats on a shelf
currentshelf = 1
shelfamount = 0
print("De kat kan steeds maar 1 of 3 stappen omhoog.\nAan jouw de taak om de uit te zoeken hoevaak de kat moet springen en hoe hij dit gaat doen.")
shelfamount = int(input("Hoeveel kasten moet de kat springen "))

while currentshelf != shelfamount:
    print(f"Je bent nu op kast {currentshelf} en je moet naar {shelfamount}")
    shelfjump = int(input("Hoe groot is de sprong die de kat moet maken"))
    if shelfjump == 1:
        print("De kat maakt een kleine sprong naar boven")
        currentshelf += 1
    elif shelfjump == 3:
        print("De kat maakt een grote sprong naar boven")
        currentshelf += 3
    elif shelfjump in (2, 4):
        print("Bonk de kat stoot zijn hoofd en beland weer op de eerste kast")
        currentshelf = 1
    else:
        print("Dit kan een kat nooit kattelijk doen!")
print("De kat is eindelijk op de kast waar hij hoort te zijn.")