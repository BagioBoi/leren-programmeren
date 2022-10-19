#Kladblok
# woord = input("Voer hier een woord in").lower()
# woord2 = ""
# for i in woord:
#     woord2 = woord2 + i + i
# print (woord2)

nummer = 50
totaal = 50
uitkomst = ""
telling = 0 
while totaal <= 1000:
    nummer += 1
    totaal += nummer
    uitkomst += f" + {nummer}"
    telling += 1
    print(f"{telling}. 50 {uitkomst} = {totaal}")