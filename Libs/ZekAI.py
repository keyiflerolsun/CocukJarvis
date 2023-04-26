# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI      import konsol
from httpx    import Client as Session
from httpx    import Cookies, Timeout
from Settings import AYAR

from Kekik.ses_fetis import ses2yazi, yazi2ses, inceses, dosya2yazi

class KekikGPT:
    def __init__(self):
        zekai_kurabiye = {
            "csrftoken" : str(AYAR["ZekAI"]["csrftoken"]),
            "sessionid" : str(AYAR["ZekAI"]["sessionid"]),
            "userid"    : str(AYAR["ZekAI"]["userid"])
        }

        kurabiyeler = Cookies()
        for isim, deger in zekai_kurabiye.items():
            kurabiyeler.set(name=isim, value=deger, domain="zekai.co", path="/")

        self.oturum = Session(
            headers = {
                "User-Agent"  : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                "Referer"     : "https://zekai.co/tr/chatbot-complete",
                "x-csrftoken" : str(AYAR["ZekAI"]["x-csrftoken"])
            },
            cookies = kurabiyeler,
            timeout = Timeout(10, connect=10, read=5*60, write=10)
        )

    def jarvis(self, prompt:str) -> str | None:
        konsol.log(f"[yellow][»] {prompt}")

        istek = self.oturum.post(
            url  = "https://zekai.co/tr/chatbot-api/v1/submit-prompt?format=json",
            data = {
                "segment"  : "chatbot-complete",
                "model"    : "auto",            # ! gpt-3.5-turbo-0301
                "sentence" : prompt
            }
        )

        if istek.status_code != 200:
            raise ValueError("ZekAI Konfigürasyon Hatası!")

        veri  = istek.json()
        cevap = veri["output2"]
        konsol.log(f"[green][+] {cevap}\n\n")

        return veri["output2"]

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
        return False

    def foto(self, prompt:str) -> str | None:
        konsol.log(f"[yellow][»] {prompt}")

        istek = self.oturum.post(
            url  = "https://zekai.co/tr/designer-api/v1/create-image",
            data = {
                "segment" : "designer-create",
                "model"   : "stable-diffusion-512-v2-1",
                "prompt"  : prompt,
                "size"    : "",
                "id"      : "",
                "steps"   : 50,
                "cfgval"  : 7
            }
        )

        if istek.status_code != 200:
            konsol.print(f"[red][!] {istek.text}")
            return None

        veri  = istek.json()
        cevap = veri["latest_create_transaction"][1]["image1_url"]
        konsol.log(f"[green][+] {cevap}\n\n")

        return cevap