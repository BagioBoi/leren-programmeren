from functionGame import *
points = 0
gameStart = True
while gameStart == True:
    startSuffering = input("Wil je beginnen met het spel of het nog een keer spelen:").lower()
    if startSuffering == "ja":
        gameActive = True
    elif startSuffering == "nee":
        gameStart = False
        gameActive = False
    while gameActive == True:
        print("Welkom bij mijn spel in dit spel zal je als timmerman of vrouw een avontuur beleven.\n")
        name = namegenerator()
        print(f"Nou {name} welkom bij je eerste dag als timmerpersoon.\nOns doel is om een prachtig hondenhok te maken.\nDaarvoor zullen we eerst hout nodig hebben.\n")
        points = plankSquareM(points)
        print("Ik hoop voor je dat je de laatste vraag en toekomstige vragen goed beantwoord.\nWant dat is belangrijk voor hoe mooi het hondenhok zal worden.\nVoordat je een hondenhok gaat maken moet je weten wat voor soort hond erin gaat leven.\nDeze ronde gaan we kijken hoeveel verschillende rassen je kan benoemen.\n")
        points = knowledgeDog(points)
        print("Nou de eerste twee opdrachten zijn gelukt(hoop ik voor je).\nOp naar de volgende en laatste stap.\nJe hebt niet zo maar een hondenhok je moet hem ook nog gaan bouwen.\n")
        points = motivated(points)
        print(points)
        if points <= -1:
            gameActive = False
        elif points == 1:
            print(f"Met geen materiaal of kennis wel de motivatie om iets te bouwen heb je nog net geen planken tegen elkaar aan gelegd en gezegd dat dit een hondenhok is.\nTotale score is{points}/3")
            gameActive = False
        elif points == 2:
            print(f"Met het materiaal of kennis en motivatie kunnen we laten zeggen dat je een hondenhok neer hebt kunnen zetten.\nTotale score is {points}/3")
            gameActive = False
        elif points == 3:
            print(f"Met materiaal en kennis en ook nog eens motivatie heb je een prachtig hondenhok neergezet de hond die hierin zal leven zal in enorme luxe leven\nTotale score is {points}/3")
            gameActive = False
print("Bedankt voor het spelen van mijn spel en hoop ik dat je het toch een beetje naar je zin hebt gehad.")