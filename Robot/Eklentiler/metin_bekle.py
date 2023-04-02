# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram       import Client, filters
from pyrogram.types import Message
from Settings       import AYAR
from Libs           import gpt

@Client.on_message(filters.text & filters.user(AYAR["Telegram"]["YETKILI"]) & filters.private & ~filters.command(["ping", "yenile"], ["!",".","/"]))
async def metin_bekle(client:Client, message:Message):
    if not message.text:
        return await message.reply("⚠️ **Lütfen metin mesajı gönderin..**")

    gonderilen_mesaj = message.text.strip()

    if gonderilen_mesaj[0] in ["!", ".", "/"]:
        return await message.reply("⚠️ **Lütfen sadece soru sorun..**")

    # < Başlangıç
    ilk_mesaj = await message.reply("⌛️ __Hemen cevaplıyorum..__",
        quote                    = True,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    cevap = gpt.jarvis(gonderilen_mesaj)
    await ilk_mesaj.delete()

    if not cevap:
        return await message.reply("⚠️ **Bir Hata Oluştu..**", quote=True, disable_web_page_preview=True)

    await message.reply(f"__{cevap}__", quote=True, disable_web_page_preview=True)