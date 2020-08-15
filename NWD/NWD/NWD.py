def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

t = int(input())
i = 0
list_of_nwd = []
while(i < t):
    a, b = (int(s)  for s in input().split())
    x = nwd(a,b)
    list_of_nwd.append(x)
    i += 1

for equals in list_of_nwd:
    print(equals)