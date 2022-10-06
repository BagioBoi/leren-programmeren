#tekst adventure "Rit naar school"
from operator import truediv
import sys
import time 

stink = False
def delay_print(s):
    #print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)

delay_print('''In dit avontuur zal je allerlij verschillende routes volgen om uiteindelijk bij een punt uit te komen.
Deze magische plek natuurlijk school.
De titel ook van dit spel is dus een inkoppertje.''')
time.sleep(1)
print('''
█▀█ █ ▀█▀   █▄░█ ▄▀█ ▄▀█ █▀█   █▀ █▀▀ █░█ █▀█ █▀█ █░░
█▀▄ █ ░█░   █░▀█ █▀█ █▀█ █▀▄   ▄█ █▄▄ █▀█ █▄█ █▄█ █▄▄ ''')
time.sleep(3)

print("Let op! een ongeldig antwoord zorgt ervoor dat je naar de 1e keuze terug gaat.")
time.sleep(5)

while True:
    avond = input('''Het verhaal begint 's avonds laat je hebt de keuze om te gaan slapen of om een stream van je favoriete streamer mee te pakken.
    Aan jou is de vraag wat doe je ''')
    if avond in ["stream", "kijk stream", "ga stream", "bekijk stream"] + ["slapen", "bed", "sleep", "ga slapen"]:
        break
    else:
        print("Dit is geen geldig antwoord") 

if avond in ["stream", "kijk stream", "ga stream", "bekijk stream"]:
    print('''Je bekijkt de stream tot diep in de nacht totdat je van vermoeidheid in slaap viel. Je wordt met paniek wakker en schrikt op uit bed. je kijkt op je wekker en ziet dat de wekker al lang af zou moeten zijn gegaan. Je beseft je dat je te laat bent en je draait jezelf om in je bed om door te slapen.
    
    Verslapen einde''')
    exit()
elif avond in ["slapen", "bed", "sleep", "ga slapen"]:
    print('Je wordt wakker gemaakt door je wekker je voelt je goed na een lange nachtrust. Je beseft je dat je al een tijd niet meer hebt gedoucht of in bad bent geweest.')



while True:
    douchen = input("Je kan nu de keuze maken of je jezelf gelijk wilt aankleden of eerst nog even douchen.")

    if douchen in ["ga aankleden", "aankleden", "kleed aan", "trek kleren aan"]:
        print("Je springt op uit bed en kleed jezelf aan. de kleding die je gister aan had gedaan ziet er nu niet meer zo aantrekkelijk uit. Je doet nieuwe kleren aan, maar toch merk je dat je stinkt.")
        if douchen in ["ga aankleden", "aankleden", "kleed aan", "trek kleren aan"]:
            stink = True
        break
    elif douchen in ["ga douchen", "douchen", "ga badkamer", "wassen"]:
        print("Na een heerlijk verfrissende douche ben je helemaal wakker en klaar om de dag in te gaan. Voordat je de badkamer uitloopt neem je nog een laatste blik in de spiegel en denk je bij jezelf (Damn who is this sexy person doing here)")
        break
    else:
        print("Dit is geen geldig antwoord")

while True:
    plaats = input("Nu dat je jezelf hebt aangekleed merk je dat je heel veel trek hebt. Nu heb je weer de keuze of je thuis wilt ontbijten of je gaat naar de winkels voor een voorbereid ontbijtje: ").lower()
    if plaats in ["thuis", "eigen ontbijt", "ga thuis", "zelfgemaakt ontbijt"]:
        print("Ontbijt kopen in de winkels is toch veel te duur om het waard te maken. Je kijkt in de koelkast en vindt daar een pak yoghurt en in de vriezer liggen nog wat bevroren bessen. Hiermee maak je een overheerlijk ontbijt voor jezelf en smikkelt dit gelijk op.")
        thuis_activiteit = input("Nadat je zelfgemaakte ontbijtje op is heb je nog even de tijd om wat voor jezelf te doen. Je kan nog even gamen op de switch of je kan een korte workout doen: ").lower()
        if thuis_activiteit in ["gamen", "ga gamen", "ga switch", "switch", "nintendo"]:
            print("Je pakt je nindendo switch en start pokemon op. Na een tijdje spelen vindt je ineens een shiny. Deze vang je gelijk. Na even verder te gamen moet je nu wel echt weg naar school.")
            vervoer = input("Het vervoer naar school is het belangrijkste wat er is. Je kan met de fiets, bus of auto naar school toe gaan: ").lower()
            if vervoer in ["ga bus", "bus", "pak bus", "pak de bus"]:
                print ('''Je komt aan bij de bushalte en merkt dat de bus is vervallen de volgende pas over een halfuur aankomt.
                    
                Bus hokje einde''')
                exit()
            elif vervoer in ["ga fiets", "pak fiets", "fiets"]:
                print('''Je was helemaal vergeten dat je fiets een lekke band had. De bus is net vertrokken.
                    
                Lekke band einde''')
                exit()
            elif vervoer in ["auto", "ga auto", "pak de auto", "pak auto"]:
                print("Je pakt de auto om naar school toe te kunnen. Je racet als een malle naar school toe. Tuurlijk kom je dan gewoon optijd.")
                if stink == True:
                    print('''Je kwam aan op school maar niemand wilde in de buurt van je zitten omdat je naar zweet rook.
                        
                    Stinkend op school einde''')
                    exit()
                else:
                    print('''Je komt optijd aan op school en na een drukke ochtend heb je het toch gehaald.
                        
                    Voldane ochtend einde''')
                    exit()
            elif thuis_activiteit in ["workout", "sporten", "ga sporten", "ga workout", "get ripped"]:
                print("Je denkt bij jezelf dat je wel een workout nodig hebt om goed wakker te worden. Na je workout ben je helemaal verfrisd en klaar om naar school toe te gaan.")
                vervoer = input("Het vervoer naar school is het belangrijkste wat er is. Je kan met de fiets, bus of auto naar school toe gaan: ").lower()
                if vervoer in ["ga bus", "bus", "pak bus", "pak de bus"]:
                    print ('''Je komt aan bij de bushalte en merkt dat de bus is vervallen de volgende pas over een halfuur aankomt.
                    
                    Bus hokje einde''')
                    input()
                    exit()
                elif vervoer in ["ga fiets", "pak fiets", "fiets"]:
                    print('''Je was helemaal vergeten dat je fiets een lekke band had. De bus is net vertrokken.
                    
                    Lekke band einde''')
                    exit()
                elif vervoer in ["auto", "ga auto", "pak de auto", "pak auto"]:
                    print("Je pakt de auto om naar school toe te kunnen. Je racet als een malle naar school toe. Tuurlijk kom je dan gewoon optijd.")
                    if stink == True:
                        print('''Je kwam aan op school maar niemand wilde in de buurt van je zitten omdat je naar zweet rook.
                        
                        Stinkend op school einde''')
                        exit()
                    else:
                        print('''Je komt optijd aan op school en na een drukke ochtend heb je het toch gehaald.
                        
                        Voldane ochtend einde''')
                        exit()
    elif plaats in ["winkel", "ga winkel", "duur ontbijt", "gekocht ontbijt"]:
        print("Je bedenkt bij jezelf dat je jezelf wel wilt verwennen deze ochtend en dat naar de winkels gaan een slim idee is. je gaat dus naar de winkels toe om een overheeeeeerlijk ontbijt te kopen.")
        ontbijt_winkel = input("Nu dat je in de winkels bent moet je de keuze maken tussen een gezond ontbijt of ongezond ontbijt.").lower()
        if ontbijt_winkel in ["gezond", "gezond ontbijt", "healthy", "gezond winkels"]:
            print("Je bent gegaan voor een maaltijd salade. Persoonlijk begrijp ik niet hoe mensen genoeg hebben aan een maaltijd salade, maar het is jouw keuze.")
            tussendoortje = input("Na je maaltijd heb je nog de keuze om een tussendoortje te nemen. doe je dit ja of nee.").lower()
            if tussendoortje in ["ja", "ga tussendoortje", "j", "yes"]:
                print('''Je was al in een tijdsnood, omdat je naar de winkels ging en toch besloot je om een tussendoortje te kopen. Je bent nu sowieso te laat, maar daar maak je je niet druk om. je kiest ervoor om nog te genieten van je dag en niet naar school toe te gaan.
                
                Even tussen uit einde
                ''')
            if tussendoortje in ["nee", "no", "n" "ga school", "school"]:
                print("Na je maaltijd ga je naar school toe, maar beter ook want je zou het anders nooit hebben gered als je nog een tussendoortje had genomen.")
                if stink == True:
                    print('''Je kwam aan op school maar niemand wilde in de buurt van je zitten omdat je naar zweet rook.
                        
                    Stinkend op school einde''')
                    exit()
                else:
                    print('''Je komt optijd aan op school en na een drukke ochtend heb je het toch gehaald.
                        
            Voldane ochtend einde''')
            exit()
        elif ontbijt_winkel in ["ongezond", "ongezond ontbijt", "unhealthy", "ongezond winkels"]:
            print("Heb je serieus voor de ongezonde maaltijd gekozen wat moet je lichaam hier wel niet van denken zo vroeg in de ochtend. Je kiest ervoor om zo ongezond mogelijk te zijn door te ontbijten met alleen maar chips al ontbijt.")
            tussendoortje = input("Na je heerlijke maaltijd heb je nog de keuze om een tussendoortje te nemen. doe je dit ja of nee.").lower()
            if tussendoortje in ["ja", "ga tussendoortje", "j", "yes"]:
                print('''Je was al in een tijdsnood, omdat je naar de winkels ging en toch besloot je om een tussendoortje te kopen. Je bent nu sowieso te laat, maar daar maak je je niet druk om. je kiest ervoor om nog te genieten van je dag en niet naar school toe te gaan.
                
                Even tussen uit einde
                ''')
            if tussendoortje in ["nee", "no", "n" "ga school", "school"]:
                print("Na je maaltijd ga je naar school toe, maar beter ook want je zou het anders nooit hebben gered als je nog een tussendoortje had genomen.")
                if stink == True:
                    print('''Je kwam aan op school maar niemand wilde in de buurt van je zitten omdat je naar zweet rook.
                        
                    Stinkend op school einde''')
                    exit()
                else:
                    print('''Je komt optijd aan op school en na een drukke ochtend heb je het toch gehaald.
                        
            Voldane ochtend einde''')
            exit()