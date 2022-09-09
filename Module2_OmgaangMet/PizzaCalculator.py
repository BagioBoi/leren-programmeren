#Pizza calculator
#de klant kan een keuze maken uit 3 afmetingen pizza's, namelijk: small, medium en large. Voor elke afmeting wordt er gevraagd hoeveel pizza's de klant wil.
#zoek op internet naar passende prijzen voor deze pizza afmetingen en noteer deze prijzen in je applicatie
#Toon op het scherm met goede omschrijving het aantal bestelde pizza's voor elke afmeting en berekenen per afmeting de prijs uit
#Toon op het scherm de totaalprijs van alle pizza's.
#Bovenaan in de Python file noteer je als commenteer het volgende: voornaam, achternaam en opdracht: Pizza calculator
#De volgende zaken dienen ook op orde te zijn:

#leesbare layout van de code
#naamgeving is duidelijk en 'self explaining'
#er is passend commentaar toegevoegd in de code
#laat de uitkomst er uit zien als een bonnetje

print ('''Welkom bij pizza emporium ChuckECheese
De prijzen van de pizza's zijn als volgt
Voor een small(cm 25) pizza kost het €7.99
Voor een medium(cm 29) pizza kost het 12.49
Voor een large(cm 35) pizza kost het 17.49''')
#Dit laat de prijzen zien voordat je de keuze maakt in je pizza

small_pizza_prijs = 7.99
medium_pizza_prijs = 12.49
large_pizza_prijs = 17.49
#De prijzen van de pizza's

small_pizza = float (input("Hoeveel small pizza(s) wil je bestellen: "))
medium_pizza = float (input ("Hoeveel medium pizza(s) wil je bestellen: "))
large_pizza = float (input ("Hoeveel large pizza(s) wil je bestellen: "))
#De input van de aantal pizza's die iemand wilt

small_cost = small_pizza_prijs * small_pizza 
medium_cost = medium_pizza_prijs * medium_pizza
large_cost = large_pizza_prijs * large_pizza
#Deze code zorgt voor een simpele uitkomst die makkelijk te verwerken is in een print

total_cost = large_cost + medium_cost + small_cost
#Deze code is voor het totale aantal wat de klant moet betalen

round_small = round(small_cost, 2)
round_medium = round(medium_cost, 2)
round_large = round(large_cost, 2)
round_total = round(total_cost, 2)
#deze code zorgt ervoor dat het tot 2 achter de , afgerond wordt

print (f'''------------------------------------------------------
Te betalen voor de small pizza is {round_small} euro
Te betalen voor de medium pizza is {round_medium} euro
Te betalen voor de large pizza is {round_large} euro

Totaal te betalen is {round_total} euro

Bedankt voor het eten bij ChuckECheese
------------------------------------------------------''')
#Deze code rekent alles uit en laat het eruit zien als een bonnetje.