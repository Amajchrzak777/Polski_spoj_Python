N = (int)(input())
#if ((N < 1) | (N >= 20)):
#    N = (int)(input())    
#else:
#    pass

x = 0
suma = 0
d = []
e = 0
while(x < N):
    a, b = (int(s)  for s in input().split())
    #if((a < 10) | (b > 30)):
    #        a, b = (int(s)  for s in input().split())
    #else:
    #    pass
    c = a+b
    e = max(a,b)
    d.append(e)
    suma += c
    x += 1  

print(suma)

if (d[0] > d[1]):
    print(d[0])
else:
    print(d[1])