from functionGame import *
gameActive = True


while gameActive == True:
    print("Welkom bij mijn spel in dit spel zal je als timmerman of vrouw een avontuur beleven.")
    name = namegenerator()
    print(f"Nou {name} welkom bij je eerste dag als timmerpersoon.\nOns doel is om een prachtig hondenhok te maken.\nDaarvoor zullen we eerst hout nodig hebben.")
    plankSquareM()
    ## print (points)/ Hier zal ik de points na het uitvoeren van de function optellen
    