n=int(input("n:"))
prim=''
cheia=0
suma=0
for x in range (1,(n//2)+1):
    if n%x==0:
        suma+=x
if suma>1:
    for i in range(2,(suma//2)+1):
        if suma%i==0:
            break
        else:
            prim='prim'
if prim=='prim':
    for x in str(suma):
        cheia+=int(x)
else:
    for x in str(n):
        if int(x)%2!=0:
            cheia+=int(x)
print(cheia)