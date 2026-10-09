print("Vecuma grupa")

vecums = int(input("Ievadi savu vecumu: "))
if vecums <=6:
    grupa= "bērns"
elif vecums <=17:
    grupa= "pusaudzis"
elif vecums <= 66:
    grupa= "pieaugušs"
elif vecums >=67:
    grupa= "seniors"

# TODO: ar if, elif un else nosaki pareizo vecumu


print(f"Jusu vecuma grupa ir {grupa}.")

