from platform import java_ver


print('speeltuin entree')

# welkom voor kinderen van 12 of onder de 12, maar alleen met een begeleider van 20 of ouder
# of welkom als ze onder de 14 zijn en een speeltuinpasje hebben
# of welkom als ze een begeleider hebben met de naam Vladimir 

# if age <= 12 : # maak de conditie correct!
#   print('welkom')
# else:
#   print('sorry, niet welkom')

leeftijd = int(input("Hoe oud ben je"))
pasje = input("Heb je een pasje").lower()
begeleider = input("Heb je een begeleider bij je").lower()
if begeleider == "ja":
  leeftijd_begeleider = int(input("Hoe oud is de begeleider"))
  naam_begeleider = input("En wat is de begeleider zijn/haar naam").lower()
pass

if (leeftijd <= 12 and begeleider == "ja" and leeftijd_begeleider >= 20) or (leeftijd <= 14 and pasje == "ja") or (naam_begeleider == "vladimir"):
  print("U bent welkom")
else:
  print("U bent niet welkom")
