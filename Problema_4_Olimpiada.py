n=int(input("n:"))
lista=[]
lista1=[]
pastila=0
i=1
if n>2:
    for x in range(1,n+1):
        nr=int(input("inaltimea:"))
        lista.append(nr)
    for x in range(0,len(lista)-1):
        if abs(lista[x]-lista[x+1])>1:
            pastila+=1
            diferenta=abs(lista[x]-lista[x+1])
            lista1.append(diferenta)
    print("numar minim de pastile=",pastila)
    print('diferenta maxima=',max(lista1))