nr=0
nr1,nr2=int(input(":")),int(input(":"))
if (nr1>1 and nr1<9999) and (nr2>1 and nr2<9999):
  nr1=str(nr1)
  nr2=str(nr2)
  if len(nr1)==4 and len(nr2)==4:
    if nr1[0]!=nr2[0]:
      nr+=1
    if nr1[1]!=nr2[1]:
      nr+=1
    if nr1[2]!=nr2[2]:
      nr+=1
    if nr1[3]!=nr2[3]:
      nr+=1
  elif len(nr1)==3 and len(nr2)==3:
    if nr1[0]!=nr2[0]:
      nr+=1
    if nr1[1]!=nr2[1]:
      nr+=1
    if nr1[2]!=nr2[2]:
      nr+=1
  elif len(nr1)==2 and len(nr2)==2:
    if nr1[0]!=nr2[0]:
      nr+=1
    if nr1[1]!=nr2[1]:
      nr+=1 
  elif len(nr1)==1 and len(nr2)==1:
    if nr1[0]!=nr2[0]:
      nr+=1    
print(nr,'cifre')
