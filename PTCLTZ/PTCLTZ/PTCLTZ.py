t = int(input())
i=0
while i < t:
    x = int(input())
    j = 0
    while x!=1:
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x+1
        j += 1
    i += 1
    print(j)
