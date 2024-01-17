from copyreg import pickle
import math
from operator import truediv
from pickle import TRUE
from xml.etree.ElementTree import PI


print("Tere maailm!")
nimi=input("Mis on sinu nimi?")
vanus=int(input("Kui vana sa oled?"))# kommentaar

print("Tere "+nimi+"! sa oled "+str(vanus)+"aastat vana.")
print("Tere",nimi,"! Sa oled",vanus,"aastat vana.")
print("Tere {0}! Sa oled {1} aastat vana".format(nimi,vanus))

print(type(nimi))
print(type(vanus))

arv1=float(input("Arv 1: "))
t=input("Tehe: ")
t=input("Arv 2:")
vastus=eval(str(arv1)+t+str(arv2))
print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))

print("Tere,maailm!")
nimi=input("Mis on sinu nimi?")
print("Tere maailm!Tervitan sind Mati")

vanus = 18
eesnimi ="Jaak"
pikkus= 16.5
kas_käib_koolis=True
print("Muutuja",vanus,"on",type(vanus))
print("Muutuja",pikkus,"on",type(pikkus))
print("Muutuja",kas_käib_koolis,"on",type(kas_käib_koolis     

#3
from random import * #kõik funktsioonid mis on moodulis
kogus=randint(1,100)
print("Kokku on",kogus,"kommid")
mitu=int(input("Mitu komi tahad võtta?")) #33
kogus=kogus-mitu #kogus=kogus-mitu=66-33 kogus=kogus-mitu->kogus-=mitu
print("Laua peal on",kogus,"kommid")

#4
from math import *
l=float(input("Ümbermõõt:"))
d=round(l/pi,2)
print("Läbimõõt=", d)

#5
import math
N=float(input("Sisestage lõigu pikkus meetrites (N): "))
M=float(input("Sisestage krundi laius meetrites (M): "))
#diagonaali pikkuse arvutamine
diagonal_length = math.sqrt(N**2 + M**2)
#väljund tulemus
print(f"Ristkülikukujulise maatüki diagonaalpikkus: {diagonal_length} meetrit.")

#6
time = float(input("Mitu tundi reis kestis?"))
tee_pikkus = float(input("Mitu kilomeetrit oled läbinud?"))
kiirus = time / tee_pikkus
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#7
# Küsime kasutajalt viis täisarvu
arv1 = int(input("Sisestage esimene arv: "))
arv2 = int(input("Sisestage teine arv: "))
arv3 = int(input("Sisestage kolmas arv: "))
arv4 = int(input("Sisestage neljas arv: "))
arv5 = int(input("Sisestage viies arv: "))

# Arvutame aritmeetilise keskmise
keskmine = (arv1 + arv2 + arv3 + arv4 + arv5) / 5

# Väljastame tulemuse
print("Sisestatud arvude aritmeetiline keskmine on:", keskmine)

#8
   print@..@
   print(----)
  print( \__/ )
print^^ "" ^^

#9
# Sisestame kolmnurga külgede pikkused
a = int(input("Sisestage esimese külje pikkus (a): "))
b = int(input("Sisestage teise külje pikkus (b): "))
c = int(input("Sisestage kolmanda külje pikkus (c): "))

# Arvutame kolmnurga ümbermõõdu
ümbermõõt = a + b + c

# Väljastame tulemuse
print("Kolmnurga ümbermõõt on:", ümbermõõt)

#10
# Pitsa hind
pitsa_hind = 12.90

# Jootraha protsent
jootraha_protsent = 10

# Arvutame jootraha summa
jootraha_summa = (jootraha_protsent / 100) * pitsa_hind

# Kogusumma iga sõbra kohta (pitsa hind + jootraha)
kogusumma_üks_inimene = pitsa_hind + jootraha_summa

# Küsime, mitu sõpra jagab arvet
sõprade_arv = int(input("Mitu inimest jagab pitsa arvet? "))

# Arvutame, kui palju igaüks peab maksma
summa_iga_inimene = kogusumma_üks_inimene / sõprade_arv

# Väljastame tulemuse
print(f"Igaüks peab maksma {summa_iga_inimene:.2f} eurot.")









