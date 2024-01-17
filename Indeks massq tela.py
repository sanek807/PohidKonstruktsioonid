print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(nimi + ", oi kui ilus nimi!")
vastus = input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if vastus==1:
    pikkus=int(input("Pikkus: "))
    mass=input(input("Mass: "))
    indeks=int(input("Indeks: " mass / (0.01 * pikkus) ** 2))



