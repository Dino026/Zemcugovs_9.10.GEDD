daudzums= int(input("cik skaitlu ievadisi:"))

if daudzums <=0:
    print("skaitlu skaitam jabut lielakam par 0")

else:
    skaitlis = int(input("ievadi skaitlus:"))
    mazakais = skaitlis
    lielakais = skaitlis

    for i in range( daudzums-1 ):
        skaitlis=int(input("ievadi skaitlu:"))
        if skaitlis<mazakais:
            mazakais = skaitlis

        if skaitlis > lielakais:
            lielakais = skaitlis

    print("mazakais", mazakais)
    print("lielakais", lielakais)