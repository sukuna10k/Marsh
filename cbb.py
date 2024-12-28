#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴘʀᴏᴘʀɪéᴛᴀɪʀᴇ : <a href='tg://user?id={OWNER_ID}'>🇰ιηg¢єу</a>\n○ ᴍᴇꜱ ᴍɪꜱᴇꜱ à ᴊᴏᴜʀ : <a href='https://t.me/Otakukingcey1'>Kingcey bot</a>\n○ ᴍɪꜱᴇꜱ à ᴊᴏᴜʀ ᴅᴇꜱ ꜰɪʟᴍꜱ: <a href='https://t.me/AntiFlix_actu'>ᴛᴇᴀᴍ ɴᴇᴛꜰʟɪx</a>\n○ ɴᴏᴛʀᴇ ᴄᴏᴍᴍᴜɴᴀᴜᴛé : <a href='https://t.me/Anime_Crow'>Anime Crow</a>\n○ ᴄʜᴀᴛ ᴀɴɪᴍᴇ : <a href='https://t.me/kingcey1'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ꜰᴇʀᴍᴇʀ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/otakukingcey1/53')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
