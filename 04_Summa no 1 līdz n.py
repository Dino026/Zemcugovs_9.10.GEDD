n= int(input("ievadi pozitivu veselu skaitlu:"))
try:
    if n<0:
        print("Tas ir negativais skairlis")
    elif n==0:
        print("Tas nav vesels skaitlis")
    else:
        endsum=0
        for i in range (0, n):
            endsum += (i+1)
        print(endsum)

except ValueError:
    print("Tas nav skaitlis")