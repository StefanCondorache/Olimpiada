n=int(input("numarul de fasii:"))
l=[]
nr,true=0,False
if n>=1 and n<=100:
    for x in range(1,n+1):
        a=str(input("numarul:"))
        l.append(a)
    for x in l:
        if x[0].startswith('0'):
            nr+=1
    if nr==len(l):
        print("Cel puţin unul din fragmente începe cu o cifră diferită de 0")
    else:
        for x in l:
            if len(x)>=1 and len(x)<=100:
                true=True
            else:
                true==False
            if true==False:
                print('şir de cifre de la 1 la 100')
                break
