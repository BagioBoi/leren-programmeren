scoreE = int (input("Hoeveel punten heb je behaald voor exelente acties?: 0 tm/6 "))
scoreP = int (input("Hoeveel punten heb je behaald voor professionele acties?: 0 tm/8 "))
scoreO = int (input("Hoeveel punten heb je behaald voor onprofessionele acties?: 0 tm/5  "))
scoreS = int (input("Hoeveel punten heb je behaald voor slechte acties?: 0tm/ 2 "))

# while True:
#     try:
#         scoreE int(input("Hoeveel punten heb je behaald voor je exelente acties?: "))

totalScore = scoreE + scoreP - scoreO - scoreS

if scoreE >= 4 and scoreP == 8 and scoreO == 0 and scoreS == 0:
    print("U hebt een Goed gebehaald voor uw examen")
elif scoreS == 0 and totalScore >= 7 and totalScore <= 13 or scoreS == 1 and totalScore >= 9:
    print("U hebt een Voldoende behaald voor uw examen") 
elif scoreS == 2 or totalScore <= 7:
    print("U hebt een Onvoldoende behaald voor uw examen")
else:
    print("U heeft niet geldige gegevens ingevoerd")
