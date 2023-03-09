from functionGame import *
gameStart = True
while gameStart == True:
    startSuffering = input("Wil je beginnen met het spel of het nog een keer spelen").lower()
    if startSuffering == "ja":
        gameActive = True
    elif startSuffering == "nee":
        gameActive = False
    while gameActive == True:
        print("Welkom bij mijn spel in dit spel zal je als timmerman of vrouw een avontuur beleven.\n")
        name = namegenerator()
        print(f"Nou {name} welkom bij je eerste dag als timmerpersoon.\nOns doel is om een prachtig hondenhok te maken.\nDaarvoor zullen we eerst hout nodig hebben.\n")
        points = plankSquareM()
        print("Ik hoop voor je dat je de laatste vraag en toekomstige vragen goed beantwoord.\nWant dat is belangrijk voor hoe mooi het hondenhok zal worden.\nVoordat je een hondenhok gaat maken moet je weten wat voor soort hond erin gaat leven.\nDeze ronde gaan we kijken hoeveel verschillende rassen je kan benoemen.\n")
        points += knowledgeDog()
        print("Nou de eerste twee opdrachten zijn gelukt(hoop ik voor je).\nOp naar de volgende en laatste stap.\nJe hebt niet zo maar een hondenhok je moet hem ook nog gaan bouwen.\n")
        motivated()
        if points == -1:
            gameActive = False