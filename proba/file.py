#%%
# 3, propitati
# asdasd
# dodaj jos
import random


def igramo_kpm():
    igrač = ""
    while igrač != "e":
        igrač = input("pritisni k za kamen,p za papir,m za makaze, šta biraš?")
        računar = random.choice(["k", "p", "m"])
        print(f"ja sam odabrao {računar}.")

        if igrač == računar:
            return "rezultat je neriješen"

        if igrac_je_pobjedio(igrač, računar):
            return "ti si pobjednik!"

        return "ja sam pobijedio"


# k>m, m>P  , p>k
def igrac_je_pobjedio(igrač, računar):
    if (
        (igrač == "k" and računar == "m")
        or (igrač == "m" and računar == "p")
        or (igrač == "p" or računar == "k")
    ):
        return True


print(igramo_kpm())
