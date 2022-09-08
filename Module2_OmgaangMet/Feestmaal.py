#Stel: je organiseert een ‘Feestlunch’
# Je wilt 17 croissantjes van elk 39 eurocent en 2 stokbroden van elk 2,78 euro kopen. Je hebt 3 kortingsbonnen van 50 eurocent. 
# Hoeveel geld moet je betalen?
#Maak een programma feestlunch.py voor deze berekening.
#Lever hier het programma in en vergeet ook niet te committen en pushen!


croissantaantal = int(input ('Hoeveel croissant(s) wil je kopen: '))
croissant = 0.39
stokbroodaantal = int(input ('Hoeveel stokbroden wil je kopen: '))
stokbrood = 2.78
kortingaantal = int(input ("Hoeveel kortingsbonnen heb je: "))
korting = 0.50

prijs = (((croissantaantal * croissant) + stokbroodaantal * stokbrood) - kortingaantal * korting)


print ('De feestlunch kost je bij de bakker',{prijs}, 'euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn')

