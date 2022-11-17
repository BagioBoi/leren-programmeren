import random
MMkleur = ("oranje", "blauw", "groen", "bruin")
MMkeuze = int(input("Hoeveel M&M's moeten er in de zak"))
MMzak = []

while MMkeuze > 0:
    MMzak += random.choices(MMkleur)
    MMkeuze -= 1
print(f"Er zitten zoveel M&M's in de zak {MMzak}")
