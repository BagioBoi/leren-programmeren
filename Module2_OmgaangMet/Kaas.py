geel = input ("Heeft u gele kaas ja/nee: ")

if geel == "ja": 
    gaten = input ("Zitten er gaten in de kaas ja/nee: ")

    if gaten == "ja":
        duur = input ("Is de kaas belachelijk duur ja/nee: ")

        if duur == "ja":
            print ("Emmenthaler")
        else: 
            print ("Leerdammer")

    else:
        steen = input ("Is de kaas hard als steen ja/nee: ")

        if steen == "ja": 
            print ("Parmigiana Reggiona")
        else:
            print ("Goudse Kaas")

if geel == "nee": 
    schimmel = input ("Zit er schimmel op de kaas ja/nee: ")

    if schimmel == "ja":
        korst = input ("Heeft de kaas een korst ja/nee: ")

        if korst == "ja":
            print ("Blue de Rochbaron")
        else:
            print ("Foume d'Ambert")

    if schimmel == "nee":
        korst2 = input ("Heeft de kaas een korst ja/nee: ")

        if korst2 == "ja":
            print ("Camembert")
        else: 
            print ("Mozzarella")

