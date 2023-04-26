# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram       import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction
from Settings       import AYAR
from Libs           import gpt
from os             import remove

@Client.on_message(filters.voice & filters.user(AYAR["Telegram"]["YETKILI"]))
async def ses_dinle(client:Client, message:Message):
    # < Başlangıç
    ilk_mesaj = await message.reply("⌛️ __Hemen cevaplıyorum..__",
        quote                    = True,
        disable_web_page_preview = True
    )
    #------------------------------------------------------------- Başlangıç >

    await client.send_chat_action(message.chat.id, ChatAction.RECORD_AUDIO)

    gelen_ses = await client.download_media(message)
    ses_dosyasi, cevap_metni = gpt.dinle_ve_cevap_ver(gelen_ses)

    metin = f"__{cevap_metni}__"

    if len(metin) < 1024:
        await message.reply_voice(ses_dosyasi, caption=f"__{cevap_metni}__")
    elif len(metin) < 4096:
        await message.reply_text(f"__{cevap_metni}__")
        await message.reply_voice(ses_dosyasi)
    else:
        await message.reply_voice(ses_dosyasi)

    remove(gelen_ses)
    await ilk_mesaj.delete()
    remove(ses_dosyasi)