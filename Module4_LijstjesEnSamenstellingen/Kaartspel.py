#Kaartspel
import random
kaartWaarde = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Koning", "Aas")
kaartVorm = ("Harten", "Schoppen", "Klaveren", "Ruiten")
deck = []
for x in kaartVorm:
    for i in kaartWaarde:
        deck.append(f"{x} {i}")
deck.append("JokerR")
deck.append("JokerZ")
random.shuffle(deck)
print(deck[0:7])
for x in range(7):
    print(x + 1, deck[0])
    deck.pop(0)
print(deck)

#Kaart toevoegen in deck na 7x 
#Joker er in appenden(toevoegen)