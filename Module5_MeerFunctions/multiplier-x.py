#multiplier-x

def tafelRekenen(x):
    result = ""
    for i in range (1, 11):
        result += f"{i} x {x} = {i * x}\n"
    return result

cijfer = int(input("Welke tafel wil je uitgerekend hebben"))
print (tafelRekenen(cijfer))