#N = int(input('Liczba testów'))
#i = 0
#list_of_napis = []
#while(i < N):
#    napis = input()
#    i += 1
#    list_of_napis.append(napis)

    
#for n in list_of_napis:
#    print(n)

napis = "AAADAM"

#print(napis)
i = 2
j = 0
x = 0
lista_pojedynczych_znakow = []
while(napis != '\n'):
    while((napis[i]==napis[i-1]) & (napis[i] == napis[i-2])):
        #if (napis[i] == napis[i-2]):
        lista_pojedynczych_znakow.append(napis[i])
        j += 1
        i += 1
    lista_pojedynczych_znakow[x] = j
    j = 0
    x += 1
    print(napis[i])
    i += 1