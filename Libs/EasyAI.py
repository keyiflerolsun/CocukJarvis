# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kekik.cli import konsol
from httpx     import Client as Session
from httpx     import Timeout
from os        import urandom
from json      import loads

class KekikGPT:
    def __init__(self):
        self.session_id = urandom(10).hex()

        self.oturum = Session(
            headers = {
                "Accept"          : "text/event-stream",
                "Accept-Language" : "tr-TR,tr;q=0.9,en-US;q=0.7,fr-FR;q=0.5",
                "Cache-Control"   : "no-cache",
                "Connection"      : "keep-alive",
                "Pragma"          : "no-cache",
                "Referer"         : "http://easy-ai.ink/chat",
                "User-Agent"      : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "token"           : "null",
            },
            timeout = Timeout(10, connect=10, read=5*60, write=10)
        )

    def chat(self, prompt):
        params = {"message": prompt, "sessionId": self.session_id}

        with self.oturum.stream("GET", "http://easy-ai.ink/easyapi/v1/chat/completions", params=params) as istek:
            for chunk in istek.iter_lines():
                if "content" in chunk:
                    veri = loads(chunk.split("data:")[1])
                    yield veri["content"]

gpt = KekikGPT()
while True:
    prompt = konsol.input("\n\n[yellow]» : ")
    konsol.print("[green]~ : ", end="")
    for result in gpt.chat(prompt):
        konsol.print(result, end="")