# tekst= """En ze stu[re]n [i]ngekleurde prentbriefkaarten van plekken waarvan ze zich niet reali[s]eren dat ze er nooit geweest zijn [a]an ' Iedereen op nummer 22, weer is prachti[g], onz[e] kamer is aa[n]gekruisd. Missen jullie. E[t]en[ ]i[s] vettig , maar we hebben een geweldig leuk restaurantje gevonden in de achterstraatjes waar ze Heine[ke]n hebben en kaas en uien chips en iemand die "Een beetje verliefd" speel[t] op een a[c]cordeon ' en je zit vier dagen vast op Schip[h]ol voor je vijfdaagse vliegvakantie met niks anders te eten dan uitgedroogde voorverpakte boterhammen..."""

# def function(tekst):
#     geheimschrift = ""
#     filter = False
#     for str in tekst:
#         if str == "[":
#             filter = True
#         elif str == "]":
#             filter = False
#         elif filter == True:
#             geheimschrift += str
#     return geheimschrift

# bericht = function(tekst)
# print(bericht)

    
# def number_to_pwr(number, p): 
#     orignumber = number
#     if p == 0:
#         number = 1
#     for p in range(p-1):
#         number *= orignumber
#     return number

# prijsSpel = 24.95
# korting = 0.6
# kosten = 0
# totaalSpellen = int(input("Hoeveel spellen wil je hebben?"))
# for verkochteSpellen in range (totaalSpellen):
#     if verkochteSpellen == 0:
#         kosten += (prijsSpel * korting) + 1
#     else:
#         kosten += (prijsSpel * korting) + 0.25
# print (round(kosten,2))

prijsSpel = 24.95
korting = 0.6
# kosten1eSpel = 15.97
# kostenRest = 15.22
totaalSpellen = int(input("Hoeveel spellen wil je? "))
kosten1eSpel = (prijsSpel * korting) + 1
kostenOverig = (prijsSpel * korting) + 0.25
kostenTotaalRest = kostenOverig * (totaalSpellen -1)
totaalPrijs = kostenTotaalRest + kosten1eSpel
print(totaalPrijs)
