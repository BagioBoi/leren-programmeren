# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #wisselgeld wordt hier automatisch in centen berekend
toprint = ""

if change > 0: #Als je nog geld moet terug geven dan runt het deze code
  coinValue = 500 #Dit zorgt ervoor dat je het wisselgeld met vaste aantallen kan terugbetalen
  
  while change > 0 and coinValue > 0: # Als er nog "change" is en de coinValue is groter dan nul zal deze code runnen. !Letop hier moet ook coinValue groter dan nul zijn en niet alleen de "change"
    nrCoins = change // coinValue # Hier laat het zien hoeveel "coins" je kan terug geven door "change" te delen en naar beneden af te ronden.

    if nrCoins > 0: # Als het aantal wat je nog qua "coins" terug kan geven groter is dan nul dan zal het de volgende code runnen
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Hier geeft het aan hoeveel "coins" je van een bepaalde value terug kan geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Laat zien hoeveel "coins" je terug hebt gegeven nadat je iets hebt ingevuld bij het terug geven van een "coin" bij een bepaalde value
      change -= nrCoinsReturned * coinValue # Hier rekent het uit hoeveel er van het totaal wat je nog moet betalen af wordt gehaald.
      totaalreturned = nrCoinsReturned
      totaalvalue = coinValue
      toprint += f"coins returned: {totaalreturned} van {totaalvalue} cents\n" # hetzelfde als toprint = toprint + ..

# comment on code below: Dit zorgt ervoor dat je het wisselgeld met vaste aantallen kan terugbetalen.
# Als een aantal is ingevuld bij het teruggeven van wisselgeld gaat het gelijk naar de volgende.
# Wanneer er iets is ingevuld van het teruggeven van geld rekent het gelijk uit hoeveel er nog te betalen is.
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # Als change aan het einde nog groter is dan nul zal het aangeven hoeveel je nog moet terug betalen. en anders laat het zien hoeveel je van bepaalde munten hebt terug gegeven.
  print('Change not returned: ', str(change) + ' cents')
else:
  print(toprint)