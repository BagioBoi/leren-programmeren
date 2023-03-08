#guldenSnede

hoevaak = int(input("Hoe veel getallen wil je van de fibonacci reeks zien: "))
def fibonacciReeks(hoevaak):
    n1 = 0
    n2 = 1
    fibo = []
    for x in range(0, hoevaak):
        fibo.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
    return fibo
fibo = fibonacciReeks(hoevaak)
guldenSnede = len(fibo)
print(f"Dit is de reeks van fibonacci")
print(fibo)
print(f"De som van de gulden snede is {fibo[guldenSnede -1]} / {fibo[guldenSnede -2]}")
print(f"De gulden snede is {fibo[guldenSnede-1] / fibo[guldenSnede-2]}")

