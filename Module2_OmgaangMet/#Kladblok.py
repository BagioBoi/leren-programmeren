#Kladblok
from random import randint
herhaling = 0
naam = input ("Wat is je naam: ")
hoeveel_complimenten = int(input("Hoeveel complimenten wil je: "))

for x in range(hoeveel_complimenten):
    random_getal = randint(1, 4)
    while random_getal == herhaling:
        random_getal = randint(1, 4)
    if random_getal == 1:
        print(f"Je bent geweldig {naam}")
    elif random_getal == 2:
        print(f"Je bent de beste {naam}")
    elif random_getal == 3:
        print(f"Je bent super lief {naam}")
    else:
        print(f"Je bent super cool {naam}")
    herhaling = random_getal

    