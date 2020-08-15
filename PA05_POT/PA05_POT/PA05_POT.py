N = int(input())
list_of_exponentionals = []
i = 0
while(i < N):
    a, b = (int(s) for s in input().split())
    i += 1
    c = a**b
    list_of_exponentionals.append(str(c))

for s in list_of_exponentionals:
    print(s[-1])