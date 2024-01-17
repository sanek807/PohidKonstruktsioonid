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
# Küsime kasutajalt pikkust
pikkus = float(input("Sisestage oma pikkus meetrites: "))

# Määrame piirid lühikese, keskmise ja pika jaoks
lühike_pikkus = 1.6  # Näide, millest allapoole on lühike
pikk_pikkus = 1.8   # Näide, millest ülespoole on pikk

# Kontrollime, millisesse kategooriasse kasutaja kuulub
if pikkus < lühike_pikkus:
    print("Te olete lühike.")
elif lühike_pikkus <= pikkus <= pikk_pikkus:
    print("Te olete keskmise pikkusega.")
else:
    print("Te olete pikk.")
    
#7
# Küsime kasutajalt pikkust ja sugu
pikkus = float(input("Sisestage oma pikkus meetrites: "))
sugu = input("Sisestage oma sugu (mees/naine): ").lower()

# Määrame piirid lühikese, keskmise ja pika jaoks
lühike_pikkus = 1.6  # Näide, millest allapoole on lühike
pikk_pikkus = 1.8   # Näide, millest ülespoole on pikk

# Kontrollime, millisesse kategooriasse kasutaja kuulub, võttes arvesse sugu
if sugu == "mees":
    if pikkus < lühike_pikkus:
        print("Te olete lühike mees.")
    elif lühike_pikkus <= pikkus <= pikk_pikkus:
        print("Te olete keskmise pikkusega mees.")
    else:
        print("Te olete pikk mees.")
elif sugu == "naine":
    if pikkus < lühike_pikkus:
        print("Te olete lühike naine.")
    elif lühike_pikkus <= pikkus <= pikk_pikkus:
        print("Te olete keskmise pikkusega naine.")
    else:
        print("Te olete pikk naine.")
else:
    print("Palun sisestage kehtiv sugu (mees/naine).")

#8
import random

# Määrame tooted ja nende juhuslikud hinnad
tooted = {
    "piim": random.uniform(0.5, 2.5),
    "sai": random.uniform(1, 3),
    "leib": random.uniform(1.5, 4),
    # Lisage teisi tooteid vajadusel
}

# Küsime kasutajalt, mida ta soovib osta
ostukorv = {}
for toode, hind in tooted.items():
    kysimus = f"Kas soovite osta {toode}? (jah/ei): "
    vastus = input(kysimus).lower()
    if vastus == "jah":
        kogus = int(input(f"Mitu tükki {toode} soovite osta? "))
        ostukorv[toode] = {"hind": hind, "kogus": kogus}

# Arvutame ostude kogusumma
kokku_summa = sum(item["hind"] * item["kogus"] for item in ostukorv.values())

# Väljastame ostutšeki
print("\nOSTUTŠEKK:")
print("-" * 20)
for toode, andmed in ostukorv.items():
    print(f"{toode}: {andmed['kogus']} tk x {andmed['hind']:.2f} € = {andmed['kogus'] * andmed['hind']:.2f} €")
print("-" * 20)
print(f"Kokku: {kokku_summa:.2f} €")

#9
# Küsime kasutajalt ruudu küljed
kylg1 = float(input("Sisestage esimese külje pikkus: "))
kylg2 = float(input("Sisestage teise külje pikkus: "))
kylg3 = float(input("Sisestage kolmanda külje pikkus: "))
kylg4 = float(input("Sisestage neljanda külje pikkus: "))

# Kontrollime, kas tegemist on ruuduga
if kylg1 == kylg2 == kylg3 == kylg4:
    print("Tegemist on ruuduga.")
else:
    print("Need küljepikkused ei moodusta ruutu.")

#10
# Küsime kasutajalt kaks arvu
arv1 = float(input("Sisestage esimene arv: "))
arv2 = float(input("Sisestage teine arv: "))

# Küsime kasutajalt tehet
tehe = input("Valige tehe (+, -, *, /): ")

# Tuvastame ja teostame kasutaja valitud tehte
if tehe == "+":
    tulemus = arv1 + arv2
    print(f"{arv1} + {arv2} = {tulemus}")
elif tehe == "-":
    tulemus = arv1 - arv2
    print(f"{arv1} - {arv2} = {tulemus}")
elif tehe == "*":
    tulemus = arv1 * arv2
    print(f"{arv1} * {arv2} = {tulemus}")
elif tehe == "/":
    # Kontrollime, et ei jagata nulliga
    if arv2 != 0:
        tulemus = arv1 / arv2
        print(f"{arv1} / {arv2} = {tulemus}")
    else:
        print("Viga! Nulliga jagamine pole lubatud.")
else:
    print("Vigane sisend! Valige korrektne tehe (+, -, *, /).")

#11
# Küsime kasutajalt sünnipäeva
sunnipaev = int(input("Sisestage oma sünnipäeva aastaarv: "))

# Kontrollime, kas sünnipäev on juubel
if (sunnipaev - 1900) % 10 == 0:
    print("Palju õnne! Tegemist on juubeliaastaga.")
else:
    print("See aasta ei ole juubeliaasta.")

#12
# Küsime kasutajalt toote hinda
toote_hind = float(input("Sisestage toote hind: "))

# Määrame allahindluste piirid
allahindlus_10_protsenti = 10
allahindlus_20_protsenti = 20
allahindlus_piir = 10  # Piirhind, millest alates rakendatakse 20% allahindlust

# Kontrollime, millist allahindlust rakendada
if toote_hind <= allahindlus_piir:
    allahindluse_summa = (allahindlus_10_protsenti / 100) * toote_hind
    loplik_hind = toote_hind - allahindluse_summa
    print(f"Allahindlus 10%! Lõplik hind on {loplik_hind:.2f} eurot.")
else:
    allahindluse_summa = (allahindlus_20_protsenti / 100) * toote_hind
    loplik_hind = toote_hind - allahindluse_summa
    print(f"Allahindlus 20%! Lõplik hind on {loplik_hind:.2f} eurot.")

#13
# Küsime kandideerijalt soo
sugu = input("Sisestage oma sugu (mees/naine): ").lower()

# Kontrollime, kas kandideerija sobib meeskonda
if sugu == "mees":
    # Küsime vanust ainult meessoo puhul
    vanus = int(input("Sisestage oma vanus: "))

    # Kontrollime, kas vanus jääb vahemikku 16-18
    if 16 <= vanus <= 18:
        print("Tere tulemast meeskonda! Te sobite kandideerima.")
    else:
        print("Vabandame, kuid meeskonda kandideerimiseks peate olema vanuses 16-18.")
elif sugu == "naine":
    print("Tere tulemast meeskonda! Te sobite kandideerima.")
else:
    print("Vabandame, meeskond on avatud ainult meestele ja naistel ei ole vanusepiirangut.")

#14
# Küsime inimeste arvu ja bussi suurust
inimeste_arv = int(input("Sisestage inimeste arv: "))
bussi_suurus = int(input("Sisestage bussi suurus: "))

# Arvutame, mitu bussi on vaja
busside_arv = inimeste_arv // bussi_suurus

# Arvutame, mitu inimest on viimases bussis
viimase_bussi_inimesed = inimeste_arv % bussi_suurus

# Väljastame tulemuse
print(f"On vaja {busside_arv} bussi.")
print(f"Viimases bussis on {viimase_bussi_inimesed} inimest.")







   


from random import *
#4
alghind=randint(0,10000)/100 #0.00 - 1000.00
if alghind>700:
    soodustus=alghind*0.3
    alghind-=soodustus
    alghind*=0.7
print("Uus hind on",alghind)















