print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(nimi + ", oi kui ilus nimi!")
vastus = input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if vastus==1:
    pikkus=int(input("Pikkus: "))
    mass=float(input("Mass: "))
    indeks=int(input("Indeks: " mass / (0.01 * pikkus) ** 2))
    print(f"{name}! Sinu keha indeks on: {indeks:.1f}")
    if indeks_massi_tela < 16:
    vastus = "Tervisele ohtlik alakaal"
elif 16 <= indeks_massi_tela < 19:
    vastus = "Alakaal"
elif 19 <= indeks_massi_tela < 25:
    vastus = "Normaalkaal"
elif 25 <= indeks_massi_tela < 30:
    vastus = "Ülekaal"
elif 30 <= indeks_massi_tela < 35:
    vastus = "Rasvumine"
elif 35 <= indeks_massi_tela < 40:
    vastus = "Tugev rasvumine"
else:
    vastus = "Tervisele ohtlik rasvumine"







