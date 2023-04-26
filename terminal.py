# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI       import cikis_yap, hata_yakala
from playsound import playsound
from os        import remove
from Libs      import gpt

def cocuk_jarvis():
    while True:
        ses_dosyasi, cevap_metni = gpt.dinle_ve_cevap_ver()
        if not ses_dosyasi:
            continue

        playsound(ses_dosyasi)
        remove(ses_dosyasi)

if __name__ == "__main__":
    try:
        cocuk_jarvis()
        cikis_yap(False)
    except Exception as _hata:
        hata_yakala(_hata)