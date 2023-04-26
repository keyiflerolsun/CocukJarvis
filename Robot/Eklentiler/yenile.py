# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI             import log_salla
from pyrogram        import Client, filters
from pyrogram.types  import Message
from Settings        import AYAR
from Libs            import gpt
from Kekik.ses_fetis import inceses
from os              import remove

@Client.on_message(filters.command(["yenile"], ["!",".","/"]) & filters.user(AYAR["Telegram"]["YETKILI"]))
async def yenile_komut(client:Client, message:Message):
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

    yenileme_mesaji = "Çocuk Jarvis Yeniden Başlatıldı.."
    yenileme_sesi   = inceses(yenileme_mesaji, "yenileme_sesi")

    gpt.yeniden_basla()

    await message.reply_voice(yenileme_sesi, caption=f"__{yenileme_mesaji}__")
    await ilk_mesaj.delete()

    remove(yenileme_sesi)