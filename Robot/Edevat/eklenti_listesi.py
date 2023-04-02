# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI import bilgi
from os  import listdir

tum_eklentiler = [
    f"📂 {dosya.replace('.py','')}"
        for dosya in listdir("./Robot/Eklentiler/")
            if dosya.endswith(".py") and not dosya.startswith("_")
]


def eklentilerim() -> str:
    return "".join(
        f"📂 `{eklenti.replace('📂 ', '')}`\n"
            for eklenti in tum_eklentiler
    )

def eklenti_bilgi():
    eklentiler = ""
    kolon = 1
    for eklenti in tum_eklentiler:
        if kolon == 3:
            eklentiler += f"| {eklenti:<18} |\n" if len(tum_eklentiler) != 3 else f"| {eklenti:<18} |"
            kolon = 0
        else:
            eklentiler += f"| {eklenti:<18}"
        kolon += 1

    bilgi("+===============================================================+")
    bilgi("|                       Eklentilerim                            |")
    bilgi("+===============+===============+===============+===============+")
    bilgi(f"{eklentiler}")
    bilgi("+===============+===============+===============+===============+\n")