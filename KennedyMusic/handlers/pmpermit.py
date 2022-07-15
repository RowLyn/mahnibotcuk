import asyncio
from pyrogram import Client
from KennedyMusic.config import SUDO_USERS, PMPERMIT, OWNER_NAME, BOT_USERNAME, BOT_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from pyrogram import filters
from pyrogram.types import Message
from KennedyMusic.callsmusic.callsmusic import client as USER


PMSET =True
pchats = []


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(message.chat.id, f"**Salam Mən Asistanam[{BOT_NAME}](https://t me/{BOT_USERNAME}).**\n\n🔴 Note:\n\n༄ Spam Etməyin \n\n⨀ Updates Kanalı : @{UPDATES_CHANNEL} \n⨀ Support : @{GROUP_SUPPORT}\n👩‍💻 Developer : @{OWNER_NAME}\n\n")
            return

    
@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("✅ Pm İcazəsi Aktivdir")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("❌ Pm İcazəsi Aktiv Deyl")
            return


@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Şəxsi Yazışma Uğurludur")
        return
    message.continue_propagation()

 
@USER.on_message(filters.command("yes", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("✅ icazəli pm.")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("no", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("❌ icazəsiz pm")
        return
    message.continue_propagation()
