#Maak een programma person.py dat de gebruiker om zijn naam, adres, postcode en woonplaats vraagt met duidelijke prompts.
#Laat het programma daarna een adreskaart (met lijntjes) tonen in de terminal:

print ('Welkom vul hieronder uw gegeven in')

inputnaam = input("Vul hier uw naam in: ")
inputadres = input("Vul hier uw adres in: ")
inputpostcode =input("Vul hier uw postcode in: ")
inputwoonplaats =input("Vul hier uw woonplaats in: ")

print (f'''
 ----------------------------------------------------
| Naam      : {inputnaam}                
| Adres     : {inputadres}           
| Postcode  : {inputpostcode}                         
| Woonplaats: {inputwoonplaats}                          
 ----------------------------------------------------''')