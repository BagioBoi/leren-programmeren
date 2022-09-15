uren = int (input ("Hoelaat is het in uren (digitale klok): "))
minuten = int (input ("Hoelaat is het in minuten: "))

uren_einde = 23 - uren
minuten_einde = 60 - minuten

print ("Het duurt nog", uren_einde, "uur tot het einde van de dag" )
print ("Het duurt nog", minuten_einde, "minuten tot het einde van de dag")


