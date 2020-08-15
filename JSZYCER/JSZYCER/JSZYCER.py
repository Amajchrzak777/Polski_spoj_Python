szyfr = input('Podaj szyfr: ')
if len(szyfr) > 200:
    szyfr = input('Podaj szyfr: ')

x= 0
new_list = []
for digit in szyfr:
    if (ord(digit) < ord('A')) | (ord(digit) > ord('Z')):
        if (ord(digit)) == ord(' '):
            x = ord(digit)
            new_list.append(chr(x))
    else:
        if ord(digit) == 88:
            x = ord('A')
            new_list.append(chr(x))
        elif ord(digit) == 89:
            x = ord('B')
            new_list.append(chr(x))
        elif ord(digit) == 90:
            x = ord('C')
            new_list.append(chr(x))

        else:
            x = ord(digit) + 3
            new_list.append(chr(x))

print(*new_list, sep='')