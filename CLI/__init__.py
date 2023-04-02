# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kekik.cli import konsol, cikis_yap, hata_salla, log_salla, hata_yakala, bellek_temizle

def hata(yazi:str) -> None:
   konsol.print(yazi, style="bold red")
def bilgi(yazi:str) -> None:
   konsol.print(yazi, style="blue")
def basarili(yazi:str) -> None:
   konsol.print(yazi, style="bold green", width=70, justify="center")
def onemli(yazi:str) -> None:
   konsol.print(yazi, style="bold cyan")