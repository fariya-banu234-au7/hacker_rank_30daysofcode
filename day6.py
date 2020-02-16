
t = int(input())

for _ in range(t):
    s = input("Enter the string: ")
    li = list(s)
    sEven = []
    sOdd = []
    for i in range(0,len(s)):
        if i % 2 == 0:
            sEven.append(li[i])
        else:
            sOdd.append(li[i])

Evenstr = ''.join(sEven)
Oddstr = ''.join(sOdd) 
print(''.join(Evenstr ),''.join(Oddstr))
