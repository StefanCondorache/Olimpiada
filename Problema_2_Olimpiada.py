k=int(input("k:"))
n=0
suma=0
while suma<=k:
    nr=int(input("nr:"))
    n+=1
    if nr%2==0:
        suma+=nr
    if suma>k:
        print(n,suma)
        break
