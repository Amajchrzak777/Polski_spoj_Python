t = int(input())
i = 0
n = [] #lista przechowuje mi liczbe
while i < t:
    x = int(input())
    if 0 <= x <= 9 or x % 11 == 0:
        n.append(x)
        print("ta liczba jest palindromem", *n, '0')
        n = []
    else:
        j = 0
        while x % 11 != 0:
            x = str(x)
            b = int(x[::-1])
            x = int(x)
            suma = x + b
            print(suma)
            j += 1
    i += 1


t = input()
b = int(t[::-1])
print(type(b), b)