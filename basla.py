# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kekik.cli       import konsol
from yaml            import load, FullLoader
from Kekik.ses_fetis import ses2yazi, yazi2ses, inceses
from playsound       import playsound
from glob            import glob
from os              import remove
import openai

with open("AYAR.yml", "r") as yaml_dosyasi:
    AYAR = load(yaml_dosyasi, Loader=FullLoader)

openai.api_key = AYAR["OpenAI"]["API_KEY"]

mesaj_gecmisi = [
    {"role" : "system", "content" : AYAR["OpenAI"]["ROL"]}
]

def jarvis(prompt:str):
    global mesaj_gecmisi

    mesaj_gecmisi.append({"role" : "user", "content" : prompt})

    cevaplar = openai.ChatCompletion.create(
        model       = "gpt-3.5-turbo",
        max_tokens  = 1000,
        n           = 1,
        stop        = None,
        temperature = 0.7,
        messages    = mesaj_gecmisi,
    )
    cevap = cevaplar.choices[0].message["content"].strip()
    mesaj_gecmisi.append({"role" : "assistant", "content" : cevap})
    return cevap

while True:
    girdi = ses2yazi()
    konsol.log(f"[yellow][»] {girdi}")

    cevap = jarvis(girdi)
    
    konsol.log(f"[green][+] {cevap}")

    if AYAR["SESLENDIRME"]["INCE"]:
        playsound(inceses(cevap, "cevap"))
    else:
        playsound(yazi2ses(cevap, "cevap"))

    [remove(ses) for ses in glob("*.mp3")]

    konsol.print("\n")
