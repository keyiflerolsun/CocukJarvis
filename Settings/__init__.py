# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from yaml import load, FullLoader

with open("AYAR.yml", "r") as yaml_dosyasi:
    AYAR = load(yaml_dosyasi, Loader=FullLoader)