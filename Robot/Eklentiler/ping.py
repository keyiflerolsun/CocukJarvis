# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI            import log_salla
from pyrogram       import Client, filters
from pyrogram.types import Message
from Settings       import AYAR

from time import time

@Client.on_message(filters.command(["ping"], ["!",".","/"]) & filters.user(AYAR["Telegram"]["YETKILI"]))
async def ping_komut(client:Client, message:Message):

    basla = time()

    # < Başlangıç
    uye_nick         = f"@{message.from_user.username}" if message.from_user.username else None
    uye_adi          = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
    gonderilen_mesaj = message.text
    log_salla(uye_nick or uye_adi, gonderilen_mesaj, str(message.chat.type).split(".")[-1])

    ilk_mesaj = await message.reply("⌛️ `Hallediyorum..`",
        quote                    = True,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    await ilk_mesaj.delete()

    await message.reply(f"⌛️ **Tepki Süresi :** `{time() - basla:.3f}` __Saniye..__")