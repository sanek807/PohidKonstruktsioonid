#1
# Initsialiseerime tervete arvude loenduri
terved_arvud = 0

# Küsime kasutajalt 15 numbrit
for i in range(15):
    try:
        number = int(input(f"Sisestage number {i + 1}: "))
        
        # Kontrollime, kas number on tervislik (paarisarv)
        if number % 2 == 0:
            terved_arvud += 1
    except ValueError:
        print("Viga sisestamisel. Palun sisestage number.")

# Väljastame tulemuse
print(f"Neist {terved_arvud} on paarisarvud.")

#2
# Küsime kasutajalt arvu A
A = int(input("Sisestage arv A: "))

# Kontrollime, et A oleks suurem või võrdne nulliga
if A <= 0:
    print("Palun sisestage positiivne arv.")
else:
    # Leime summa naturaalarvudest 1 kuni A
    summa = sum(range(1, A + 1))

    # Väljastame tulemuse
    print(f"Kõigi naturaalarvude summa vahemikus 1 kuni {A} on: {summa}")

#3
# Initsialiseerime toote muutuja
toode = 1

# Küsime kasutajalt 8 arvu
for i in range(8):
    try:
        arv = float(input(f"Sisestage arv {i + 1}: "))
        
        # Kontrollime, kas arv on positiivne
        if arv > 0:
            toode *= arv
    except ValueError:
        print("Viga sisestamisel. Palun sisestage number.")

# Väljastame tulemuse
print(f"Positiivsete arvude toode on: {toode}")

#4
# Programm, mis kuvab arvude ruudud vahemikus 10 kuni 20

for number in range(10, 21):
    ruut = number ** 2
    print(f"Arv {number} ruudus on {ruut}")

#5
# Programm, mis kuvab arvude ruudud vahemikus 10 kuni 20

for number in range(10, 21):
    ruut = number ** 2
    print(f"Arv {number} ruudus on {ruut}")
# Programm, mis arvutab N negatiivse arvu summat

# Küsime kasutajalt N väärtust
N = int(input("Sisestage arv N: "))

# Initsialiseerime summa muutuja
summa_negatiivsed = 0

# Küsime kasutajalt N arvu ja arvutame negatiivsete arvude summa
for i in range(N):
    try:
        arv = float(input(f"Sisestage arv {i + 1}: "))
        if arv < 0:
            summa_negatiivsed += arv
    except ValueError:
        print("Viga sisestamisel. Palun sisestage number.")

# Väljastame tulemuse
print(f"Negatiivsete arvude summa on: {summa_negatiivsed}")

#6
# Programm, mis määrab negatiivsete, positiivsete ja nullide arvu

# Küsime kasutajalt N väärtust
N = int(input("Sisestage arv N: "))

# Initsialiseerime muutujad
negatiivsed = 0
positiivsed = 0
nullid = 0

# Küsime kasutajalt N arvu ja arvutame negatiivsete, positiivsete ja nullide arvu
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

# Väljastame tulemused
print(f"Negatiivsete arvude arv: {negatiivsed}")
print(f"Positiivsete arvude arv: {positiivsed}")
print(f"Nullide arv: {nullid}")

#7
# Programm, mis kuvab arvud, mis on K kordsed vahemikust [A, B]

# Küsime kasutajalt vahemiku piirid A ja B ning kordaja K
A = int(input("Sisestage vahemiku algus (A): "))
B = int(input("Sisestage vahemiku lõpp (B): "))
K = int(input("Sisestage kordaja (K): "))

# Kontrollime, et B on suurem või võrdne A-ga
if B < A:
    print("Vigane sisend. Vahemiku lõpp peab olema suurem või võrdne vahemiku algusega.")
else:
    # Kuvame arvud, mis on K kordsed vahemikus [A, B]
    print(f"Arvud, mis on {K} kordsed vahemikus [{A}, {B}]:")
    for number in range(A, B + 1):
        if number % K == 0:
            print(number)

#8
# Programm, mis prindib tabeli tollide teisendamiseks sentimeetriteks

# Prindi tabeli päis
print("Tollid\tSentimeetrid")

# Teisenda ja prindi kaugused tollidest sentimeetritesse
for tollid in range(1, 21):
    sentimeetrid = tollid * 2.54
    print(f"{tollid}\t{sentimeetrid:.2f}")

#9
# Programm sissemakse summa arvutamiseks tulevikus

# Sisestage algne sissemakse summa (S), intressimäär (r) ja aeg aastates (N)
S = float(input("Sisestage algne sissemakse summa (eurodes): "))
r = float(input("Sisestage intressimäär protsentides: "))
N = int(input("Sisestage aeg aastates: "))

# Arvutame tulevase summa
A = S * (1 + r / 100) ** N

# Väljastame tulemuse
print(f"Sissemakse summa {N} aasta pärast on {A:.2f} eurot.")

#10
# Programm, mis võrdleb ja prindib suuremad numbrid 10 numbripaarist

# Initsialiseerime listi suuremate numbrite salvestamiseks
suuremad_numbrid = []

# Küsime kasutajalt 10 numbripaari
for i in range(10):
    try:
        number1 = float(input(f"Sisestage {i + 1}. paari esimene number: "))
        number2 = float(input(f"Sisestage {i + 1}. paari teine number: "))
        suuremad_numbrid.append(max(number1, number2))
    except ValueError:
        print("Viga sisestamisel. Palun sisestage numbrid.")

# Väljastame suuremad numbrid
print("Suuremad numbrid iga paarist:")
for i, suurem_number in enumerate(suuremad_numbrid):
    print(f"Paar {i + 1}: {suurem_number}")







