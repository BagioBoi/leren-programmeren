

mbo= input("Heeft u een MBO diploma of hoger niveau? ja/nee: ")
if mbo == "ja":
    niveau = int(input("Welk MBO niveau heeft u behaald: "))
    if niveau > 4:
        mbo = True

if mbo:
    print ("hallo")
else:
    print ("Gedag")