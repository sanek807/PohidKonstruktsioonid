from random import *


a=randint(-100,100)
if a%2==0:
    print("Juhuslik arv on",a)
    print(a,"-paaris arv")

if a>0:
    print(a,"suurem kui 0")
else:
    print(a,"väiksem kui 0 või võrdne 0-ga")

#<0,>100 ei soobi,0-59-"2",60-75-"3",76-90-"4",91-100-"5"
if a<0 or a>100:
    print("Viga tulemustega!")
elif a>=0 and a<60:
    print("Hinne 2")
elif a>=60 and a<76:
    print("Hinne 3")
elif a>=76 and a<91:
    print("Hinne 4")
else:
    print("Hinne 5")


from random import *
nimi=input("Mis on sinu nimi?") #upper()-"JUKU",lower()-"juku",capitalize()-"Juku"
if nimi=="Juku":
    print("Lähme kinno")
    vanus=int(input("Kui vana sa oled"))
    if vanus<0 or vanus>120:
        vastus="Viga vanusega"
    elif vanus<6:
         vastus="tasuta"
    elif vanus<14:
        vastus="Lastepilet"
    elif vanus<65:
        vastus="täispilet"
    elif vanus<120:
        vastus="sooduspilet"
    print("On vaja Jukule osta",vastus)
else:
    print("Joonistame")

from random import *
#2 Pinginaabrid

n1=input("Esimene nimi")
n2=input("Teine nimi")
if n1.upper()=="A" and n2.upper()=="B" or n1.upper()=="B" and n2.upper()=="A":
    print("Pinginaabrid")
else:
    print("Nad ei ole naabrid")
if n1.upper() in ["A","B"] and n2.upper() in ["A","B"]:
    print("Pinginaabrid")
else:
    print("Nad ei ole naabrid")

from random import *
#3
pikkus=float(input("Põranda pikkus"))
laius=float(input("Põranda laius"))
pindala=pikkus*laius
print("Toa põranda pindala on:",pindala)
valik=input("Kas tahad remondi teha? ")
if valik.lower()=="jah":
    hind=float(input("Kui palju maksab ruuymeeter?"))
    summa=hind*pindala
    print("Põranda vahetamise summa on",summa)
    
#4
# Küsime kasutajalt alghinda
alghind = float(input("Sisestage alghind: "))

# Määratleme soodustuse protsent
soodustus_protsent = 30

# Kontrollime, kas alghind on suurem kui 700
if alghind > 700:
    # Arvutame soodustuse summa
    soodustus_summa = (soodustus_protsent / 100) * alghind

    # Arvutame soodushinnaga summa
    soodushinnaga_summa = alghind - soodustus_summa

    # Väljastame tulemuse
    print(f"30% soodustusega hind on: {soodushinnaga_summa:.2f} eurot")
else:
    # Kui alghind ei ületa 700, siis soodustust ei rakendata
    print("Alghind ei ületa 700 eurot, soodustust ei rakendata.")
    
#5
# Küsime kasutajalt temperatuuri
temperatuur = float(input("Sisestage temperatuur: "))

# Kontrollime, kas temperatuur on üle 18 kraadi
if temperatuur > 18:
    print("Temperatuur on üle 18 kraadi, see on soovitatav toasoojus talvel.")
else:
    print("Temperatuur on 18 kraadi või madalam, soovitatav on hoida soojemana talvel.")

#6




   














