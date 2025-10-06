str = input("in: ")
upperCh = [i for i,v in enumerate(str) if v == v.upper()][0]
secondCh = [i for i,v in enumerate(str) if v in '0123456789'][0]
step = secondCh - upperCh + 1
res = ''

for i in range(upperCh, len(str), step):
    res += str[i]

print(f'out: {res}')
