# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI             import konsol, hata, basarili, bellek_temizle, cikis_yap, hata_yakala
from pyrogram        import Client, __version__
from pyrogram.errors import ApiIdInvalid, AccessTokenInvalid
from sys             import version_info
from Settings        import AYAR

CocukJarvis = Client(
    name      = "CocukJarvis",
    api_id    = AYAR["Telegram"]["API_ID"],
    api_hash  = AYAR["Telegram"]["API_HASH"],
    bot_token = AYAR["Telegram"]["BOT_TOKEN"],
    plugins   = dict(root="Robot/Eklentiler"),
    in_memory = True
)

from Robot.Edevat.eklenti_listesi import tum_eklentiler

def baslangic() -> None:
    konsol.print("\n")
    try:
        CocukJarvis.start()
    except ApiIdInvalid:
        hata("\n\tAYAR.yml dosyasındaki API Bilgileri Geçersiz..\n")
        cikis_yap()
    except AccessTokenInvalid:
        hata("\n\tBot Token Geçersiz..\n")
        cikis_yap()

    surum = f"{version_info[0]}.{version_info[1]}"
    konsol.print(f"[gold1]@CocukJarvis[/] [yellow]:bird:[/] [bold red]Python: [/][i]{surum}[/]", width=70, justify="center")
    basarili(f"CocukJarvis [magenta]v[/] [blue]{__version__}[/] [red]Pyrogram[/] tabanında [magenta]{len(tum_eklentiler)} eklentiyle[/] çalışıyor..\n")

    CocukJarvis.stop()

try:
    baslangic()
    bellek_temizle()
except Exception as _hata:
    hata_yakala(_hata)