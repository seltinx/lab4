# plik = open('tekst.txt','r')
#
# znaki  = plik.read(10)
# print(znaki)
# linia = plik.readline()
# print(linia)

# import sys
# print("Podaj kierunek studiów, rok i specjalizacje")
# dane = sys.stdin.readline()
#
# plik = open('dane.txt','w+',encoding='utf-8')
#
# plik.write(dane)
#
# plik.close()
#
# lista = []
#
# for x in range(6):
#     lista.append(x)
#
# plik = open('dane.txt','a+')
#
# plik.writelines(str(lista))
#
# plik.close()

# with open('tekst.txt', 'r') as plik:
#     for linia in plik:
#         print(linia, end="")
#         print(type(linia))

# class PierwszaKlasa:
#     """Pierwsza klasa python"""
# obiekt = PierwszaKlasa()
# print(obiekt)

# Zadanie 1 #

# import random
#
# rand = []
# i = 0
# while i != 10:
#     a = random.randint(0,100)
#     if a % 4 == 0:
#         rand.append(a)
#         i += 1
# b = open('zadanie1.txt','a')
# for element in rand:
#     b.write(str(element) + '\n')
# b.close()

# Zadanie 2 #

# with open('zadanie1.txt','r') as b:
#     c = b.readlines()
#     c = [element[:-1] for element in c]
#     print(c)


# Zadanie 3 #

# with open('zadanie3.txt', 'a') as x:
#     for element in 'monsterek':
#         x.write(element + '\n')
#
# with open('zadanie3.txt', 'r') as y:
#     for element in y:
#         print(element[:-1])


# Zadanie 4 #

# class NaZakupy:
#     def __init__(self,nazwa_produktu, ilosc, jendostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jendostka_miary
#         self.cena_jed = cena_jed
#
#         def wyswietl_produkt(self):
#             return self.nazwa_produktu
#
#         def ile_produktu(self):
#             return  f'{self.ilosc} {self.jednostka_miary}'
#
#         def ile_kosztuje(self):
#             return self.ilosc * self.cena_jed
#
# xd = NaZakupy('ziemniak',1,'kg',25)
#
# print(xd.wyswietl_produkt())
# print(xd.ile_produktu())
# print(xd.ile_kosztuje())

#Cos poszło nie tak ale nie wiem co próbowałem i dałem sobie spokój#

# Zadanie 5 #

class Arytmetyczny:
    ciag = []
    ilosc = 0
    pi = 0
    r = 0

    def wyswietl_dane(self):
        return f'Elementy: {self.ciag}'

    def pobierz_parametry(self):
        self.pi = int(input("Podaj element ciągu: "))
        self.r = int(input("Podaj różnicę ciągu: "))
        self.ilosc = int(input("Podaj ilość elementów ciągudo wygenerowania: "))

    def policz_sume(self):
        return f'Suma elementów: {sum(self.ciag)}'

    def policz_elementy(self):
        self.ciag.append(self.pi)
        for x in range(1, self.ilosc):
            self.ciag.append(self.ciag[x - 1] + self.r)


xd2 = Arytmetyczny()

xd2.pobierz_parametry()
xd2.policz_elementy()
print(xd2.wyswietl_dane())
print(xd2.policz_sume())