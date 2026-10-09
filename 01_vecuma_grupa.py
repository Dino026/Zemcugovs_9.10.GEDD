print("Vecuma grupa")

vecums = int(input("Ievadi savu vecumu: "))
if vecums <6:
    grupa= "bērns"
elif vecums < 17:
    grupa= "pusaudzis"
elif vecums < 64:
    grupa= "pieaugušs"
elif vecums > 65:
    grupa= "seniors"

# TODO: ar if, elif un else nosaki pareizo vecumu


print(f"Jusu vecuma grupa ir {grupa}.")

