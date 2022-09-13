#Maak een programma dat 2 gehele getallen opvraagt aan de gebruiker. Stel die getallen zijn toegekend aan de variabelen a en b
#Bepaal (met een if-statement) of a groter is dan b
#Zo ja:
#Ken de waarde van a toe aan een variabele Max
#Laat het programma printen: ‘a is het grootste getal: ’ gevolgd door de waarde van max
#Doe een commit met de titel “input en if-statement”

#int (input("Vul hier een getal voor a in"))

a = int (input("Vul hier een getal voor a in: "))
b = int (input("Vul hier een getal voor b in: "))

if a > b:
    print ("a is groter dan b")
    print (f"Het kleinste getal is {b}")
    print (f"Het grootste getal is {a}")

elif (a==b):
    print ("a is gelijk aan b")

else:
    print ("b is groter dan a")
    print (f"Het kleinste getal is {a}")
    print (f"Het grootste getal is {b}")