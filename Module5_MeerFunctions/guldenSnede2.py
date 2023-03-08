#guldensnede2
while True:
    try:
        amount = int(input("Hoevaak wil je de fibonacci reeks herhalen: "))
        break
    except:
        print("Dat is geen geldig nummer")


def fibo(n1,n2,amount):
    while amount > 0:
        nextFibo = n1 + n2 
        n1 = n2
        n2 = nextFibo
        amount - 1
        return(nextFibo)
        
    else:
        print("Done")
fibo(0, 1, amount)
# print(0)
#Hoe haal ik steeds 1 van amount af