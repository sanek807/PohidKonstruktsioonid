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

a1=randint(1,50)
a2=randint(1,50)
a3=randint(1,50)
a4=randint(1,50)
a5=randint(1,50)

import math
N=float(input("Sisestage lõigu pikkus meetrites (N): "))
M=float(input("Sisestage krundi laius meetrites (M): "))
#diagonaali pikkuse arvutamine
diagonal_length = math.sqrt(N**2 + M**2)
#väljund tulemus
print(f"Ristkülikukujulise maatüki diagonaalpikkus: {diagonal_length} meetrit.")


