#Kladblok
stink = False

while True:
    eten = input("Nu dat je jezelf hebt aangekleed merk je dat je heel veel trek hebt. Nu heb je weer de keuze of je thuis wilt ontbijten of je gaat naar de winkels voor een voorbereid ontbijtje: ").lower()
    if eten in ["thuis", "eigen ontbijt", "ga thuis", "zelfgemaakt ontbijt"]:
        print("Ontbijt kopen in de winkels is toch veel te duur om het waard te maken. Je kijkt in de koelkast en vindt daar een pak yoghurt en in de vriezer liggen nog wat bevroren bessen. Hiermee maak je een overheerlijk ontbijt voor jezelf en smikkelt dit gelijk op.")
        if eten in ["thuis", "eigen ontbijt", "ga thuis", "zelfgemaakt ontbijt"]:
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







#     elif eten in ["winkels", "winkel", "ga winkel", "ontbijt kopen", "ga winkels", "supermarkt"]:
#         print("Laat ik maar een keer luxe doen en naar de winkels gaan om mijn ontbijt daar te kopen. Je stapt in de auto en gaat naar de winkels om daar een kant en klaar ontbijt te kopen. Je koopt een overheerlijke maaltijd salade voor jezelf.")
#         if eten in ["winkels", "winkel", "ga winkel", "ontbijt kopen", "ga winkels", "supermarkt"]:
#             stink = True
#         break
#     else:
#         print("Dit is geen geldig antwoord")

# if stink == True:
#     print("Stinky test")