from functionGame import *
gameActive = True


while gameActive == True:
    print("Welkom bij mijn spel in dit spel zal je als timmerman of vrouw een avontuur beleven.\n")
    name = namegenerator()
    print(f"Nou {name} welkom bij je eerste dag als timmerpersoon.\nOns doel is om een prachtig hondenhok te maken.\nDaarvoor zullen we eerst hout nodig hebben.\n")
    points = plankSquareM()
    print("Ik hoop voor je dat je de laatste vraag en toekomstige vragen goed beantwoord.\nWant dat is belangrijk voor hoe mooi het hondenhok zal worden.\nVoordat je een hondenhok gaat maken moet je weten wat voor soort hond erin gaat leven.\nDeze ronde gaan we kijken hoeveel verschillende rassen je kan benoemen.\n")
    points += knowledgeDog()
    print(points)