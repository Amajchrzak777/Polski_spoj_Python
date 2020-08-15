import math

tablica = [1, 1]
d = (int)(input())
if ((d >= 30) | (d <= 1)):
    d = (int)(input('Podaj ponownie d\n' ))
x = 0
wynik = []
while x < d:
    suma = 1
    tablica[x] = (int)(input())
    if((tablica[x] < 1) | (tablica[x] > 1000000000)):
        while(tablica[x] < 1):
            tablica[x] = (int)(input())
    else:
        pass
    while (tablica[x] > 1):
        suma *= tablica[x] 
        tablica[x] -= 1
    x += 1
    wynik.append(suma)

i = 0
jednosci = []
jednostka = 0
dziesiatki = []
dziesiatka = 0
for liczba in wynik:
    #if wynik[i] <= 9:
    jednostka = wynik[i] % 10
    #else:
    dziesiatka = math.floor((wynik[i] % 100)/10)
    #dziesiatka = (wynik[i] % 100)//10

    jednosci.append(jednostka)
    dziesiatki.append(dziesiatka)
    print(dziesiatki[i], jednosci[i])
    i += 1