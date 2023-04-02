# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI             import konsol
from Settings        import AYAR
from Kekik.ses_fetis import ses2yazi, yazi2ses, inceses, dosya2yazi
import openai

openai.api_key = AYAR["OpenAI"]["API_KEY"]

class KekikGPT:
    def __init__(self):
        self.mesaj_gecmisi = [
            {"role": "system", "content": AYAR["OpenAI"]["ROL"]}
        ]

    def jarvis(self, prompt:str):
        self.mesaj_gecmisi.append({"role": "user", "content": prompt})
        konsol.log(f"[yellow][»] {prompt}")

        cevaplar = openai.ChatCompletion.create(
            model       = "gpt-3.5-turbo",
            max_tokens  = 1000,
            n           = 1,
            stop        = None,
            temperature = 0.7,
            messages    = self.mesaj_gecmisi,
        )

        cevap = cevaplar.choices[0].message["content"].strip()
        self.mesaj_gecmisi.append({"role": "assistant", "content": cevap})
        konsol.log(f"[green][+] {cevap}\n\n")

        return cevap

    def dinle_ve_cevap_ver(self, ses_dosyasi:str=None):
        if ses_dosyasi:
            girdi = dosya2yazi(ses_dosyasi)
        else:
            girdi = ses2yazi(n_saniye_dinle=AYAR["SesKontrol"]["n_saniye_dinle"] or None, bip=AYAR["SesKontrol"]["bip_sesi"])

        if not girdi:
            return None, None

        cevap = self.jarvis(girdi)

        if AYAR["SesKontrol"]["ince_ses"]:
            return inceses(cevap, "cevap"), cevap
        else:
            return yazi2ses(cevap, "cevap"), cevap

    def yeniden_basla(self):
        self.mesaj_gecmisi = [
            {"role": "system", "content": AYAR["OpenAI"]["ROL"]}
        ]