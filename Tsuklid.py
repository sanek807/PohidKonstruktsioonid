#1
terved_arvud = 0
for i in range(15):
    try:
        number = int(input(f"Sisestage number {i + 1}: "))
        if number % 2 == 0:
            terved_arvud += 1
    except ValueError:
        print("Viga sisestamisel. Palun sisestage number.")


print(f"Neist {terved_arvud} on paarisarvud.")

#2

A = int(input("Sisestage arv A: "))


if A <= 0:
    print("Palun sisestage positiivne arv.")
else:
    
    summa = sum(range(1, A + 1))

    
    print(f"Kõigi naturaalarvude summa vahemikus 1 kuni {A} on: {summa}")

#3

toode = 1


for i in range(8):
    try:
        arv = float(input(f"Sisestage arv {i + 1}: "))
        
        
        if arv > 0:
            toode *= arv
    except ValueError:
        print("Viga sisestamisel. Palun sisestage number.")


print(f"Positiivsete arvude toode on: {toode}")

#4


for number in range(10, 21):
    ruut = number ** 2
    print(f"Arv {number} ruudus on {ruut}")

#5


for number in range(10, 21):
    ruut = number ** 2
    print(f"Arv {number} ruudus on {ruut}")



N = int(input("Sisestage arv N: "))


summa_negatiivsed = 0


for i in range(N):
    try:
        arv = float(input(f"Sisestage arv {i + 1}: "))
        if arv < 0:
            summa_negatiivsed += arv
    except ValueError:
        print("Viga sisestamisel. Palun sisestage number.")


print(f"Negatiivsete arvude summa on: {summa_negatiivsed}")

#6



N = int(input("Sisestage arv N: "))


negatiivsed = 0
positiivsed = 0
nullid = 0


for i in range(N):
    try:
        arv = float(input(f"Sisestage arv {i + 1}: "))
        
        if arv < 0:
            negatiivsed += 1
        elif arv > 0:
            positiivsed += 1
        else:
            nullid += 1
    except ValueError:
        print("Viga sisestamisel. Palun sisestage number.")


print(f"Negatiivsete arvude arv: {negatiivsed}")
print(f"Positiivsete arvude arv: {positiivsed}")
print(f"Nullide arv: {nullid}")

#7



A = int(input("Sisestage vahemiku algus (A): "))
B = int(input("Sisestage vahemiku lõpp (B): "))
K = int(input("Sisestage kordaja (K): "))


if B < A:
    print("Vigane sisend. Vahemiku lõpp peab olema suurem või võrdne vahemiku algusega.")
else:
    
    print(f"Arvud, mis on {K} kordsed vahemikus [{A}, {B}]:")
    for number in range(A, B + 1):
        if number % K == 0:
            print(number)

#8

print("Tollid\tSentimeetrid")


for tollid in range(1, 21):
    sentimeetrid = tollid * 2.54
    print(f"{tollid}\t{sentimeetrid:.2f}")

#9



S = float(input("Sisestage algne sissemakse summa (eurodes): "))
r = float(input("Sisestage intressimäär protsentides: "))
N = int(input("Sisestage aeg aastates: "))


A = S * (1 + r / 100) ** N


print(f"Sissemakse summa {N} aasta pärast on {A:.2f} eurot.")

#10



suuremad_numbrid = []


for i in range(10):
    try:
        number1 = float(input(f"Sisestage {i + 1}. paari esimene number: "))
        number2 = float(input(f"Sisestage {i + 1}. paari teine number: "))
        suuremad_numbrid.append(max(number1, number2))
    except ValueError:
        print("Viga sisestamisel. Palun sisestage numbrid.")


print("Suuremad numbrid iga paarist:")
for i, suurem_number in enumerate(suuremad_numbrid):
    print(f"Paar {i + 1}: {suurem_number}")
    







