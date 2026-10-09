parole = "67"
meginajumi= 3
print ("ievadi parolu")
while meginajumi >0:
    x= input()
    if(x== parole):
        print("pareizi!!!!!!!!!!!!!!!!!!!!!!!!!")
        break
    else:
        meginajumi -= 1
        print("palika meginajumu", str (meginajumi))
if meginajumi==0:
    print("piekluve ir bloketa")
