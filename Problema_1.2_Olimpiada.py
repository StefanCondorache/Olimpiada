n,nr=str(input(':')),0
l=[]    #numerele care se repeta
l1={}   #variabila si valoare
l2=[]   #numarul de repetare a numerelor
if int(n)>1 and int(n)<10**200:
    for x in range(0,10):
        if n.count(str(x))>1:
            l.append(x)
    if len(l)==1:
        print(l[0])
    elif len(l)>1:
        for x in l:
            l1[x]=n.count(str(x))
        for x in l1:
            l2.append(l1[x])
        a=max(l2)
        for x in l1:
            if l1[x]==a:
                nr+=1
        if nr==1:
            for y in l1:
                if l1[y]==a:
                    print(y)
        elif nr>1:
            print(max(l1))
