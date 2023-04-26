# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

# * https://github.com/xtekky/gpt4free/blob/main/you/__init__.py

from CLI        import konsol
from tls_client import Session
from re         import findall
from json       import loads, dumps
from uuid       import uuid4

from Settings        import AYAR
from Kekik.ses_fetis import ses2yazi, yazi2ses, inceses, dosya2yazi
from re              import sub

class KekikGPT:
    def __init__(self):
        self.mesaj_gecmisi = []

        self.client         = Session(client_identifier="chrome_108")
        self.client.headers = {
            "authority"          : "you.com",
            "accept"             : "text/event-stream",
            "accept-language"    : "tr-TR,tr;q=0.9,en-US;q=0.7,fr-FR;q=0.5",
            "cache-control"      : "no-cache",
            "referer"            : "https://you.com/search?q=who+are+you&tbm=youchat",
            "sec-ch-ua"          : '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            "sec-ch-ua-mobile"   : "?0",
            "sec-ch-ua-platform" : '"Windows"',
            "sec-fetch-dest"     : "empty",
            "sec-fetch-mode"     : "cors",
            "sec-fetch-site"     : "same-origin",
            "cookie"             : f"safesearch_guest=Moderate; uuid_guest={uuid4()}",
            "user-agent"         : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }
        self.jarvis(AYAR["OpenAI"]["ROL"], log=False)

    def jarvis(self, prompt:str, log:bool=True) -> dict:
        if log:
            konsol.log(f"[yellow][»] {prompt}")

        response = self.client.get(
            url    = "https://you.com/api/streamingSearch",
            params = {
                "q"              : prompt,
                "page"           : 1,
                "count"          : 10,
                "safeSearch"     : "Moderate",
                "onShoppingPage" : False,
                "mkt"            : "",
                "responseFilter" : "WebPages,Translations,TimeZone,Computation,RelatedSearches",
                "domain"         : "youchat",
                "queryTraceId"   : f"{uuid4()}",
                "chat"           : dumps((self.mesaj_gecmisi))
            }
        )

        serp  = findall(r"youChatSerpResults\ndata: (.*)\n\nevent", response.text)[0]
        links = findall(r"thirdPartySearchResults\ndata: (.*)\n\nevent", response.text)[0]
        # slots = findall(r"slots\ndata: (.*)\n\nevent", response.text)[0]

        text = response.text.split('}]}\n\nevent: youChatToken\ndata: {"youChatToken": "')[-1]
        text = text.replace('"}\n\nevent: youChatToken\ndata: {"youChatToken": "', '')
        text = text.replace('event: done\ndata: I\'m Mr. Meeseeks. Look at me.\n\n', '')
        text = text[:-4]

        extra = {
            "serp"  : loads(serp).get("youChatSerpResults"),
            # "slots" : loads(slots)
        }

        veri = {
            "response": text.encode("utf-8").decode("unicode-escape").strip(),
            "links"   : loads(links)["search"]["third_party_search_results"],
            "extra"   : extra,
        }

        cevap = veri["response"]
        self.mesaj_gecmisi.append({"question": prompt, "answer": cevap})
        if log:
            konsol.log(f"[green][+] {cevap}\n\n")

        return cevap

    def dinle_ve_cevap_ver(self, ses_dosyasi:str=None):
        if ses_dosyasi:
            girdi = dosya2yazi(ses_dosyasi)
        else:
            girdi = ses2yazi(n_saniye_dinle=AYAR["SesKontrol"]["n_saniye_dinle"] or None, bip=AYAR["SesKontrol"]["bip_sesi"])

        if not girdi:
            return None, None

        cevap      = self.jarvis(girdi)
        md_linksiz = sub(r"\[.*?\]\((.*?)\)", "", cevap)

        if AYAR["SesKontrol"]["ince_ses"]:
            return inceses(md_linksiz, "cevap"), cevap
        else:
            return yazi2ses(md_linksiz, "cevap"), cevap

    def yeniden_basla(self):
        self.mesaj_gecmisi = []