# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Robot.Edevat.eklenti_listesi import eklenti_bilgi

eklenti_bilgi()

from CLI   import cikis_yap, hata_yakala
from Robot import CocukJarvis

if __name__ == "__main__":
    try:
        CocukJarvis.run()
        cikis_yap(False)
    except Exception as _hata:
        hata_yakala(_hata)