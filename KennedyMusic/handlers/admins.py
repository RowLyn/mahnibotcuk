from asyncio import QueueEmpty

from KennedyMusic.callsmusic import callsmusic
from KennedyMusic.callsmusic.queues import queues
from KennedyMusic.config import BOT_USERNAME, que
from KennedyMusic.cache.admins import admins
from KennedyMusic.helpers.channelmusic import get_chat_id
from KennedyMusic.helpers.dbtools import delcmd_is_on, delcmd_off, delcmd_on
from KennedyMusic.helpers.decorators import authorized_users_only, errors
from KennedyMusic.helpers.filters import command, other_filters
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

ACTV_CALLS = []


# @Client.on_message(filters.text & ~filters.private)
# async def delcmd(_, message: Message):
#    if await delcmd_is_on(message.chat.id) and message.text.startswith("/") or message.text.startswith("!") or message.text.startswith("."):
#        await message.delete()
#    await message.continue_propagation()

# remove the ( # ) if you want the auto del cmd feature is on


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await client.send_message(
        message.chat.id,
        "✅ 𝐁𝐎𝐓 𝐘𝐄𝐍𝐈𝐋𝐄𝐍𝐃𝐈 !\n\n• 𝐀𝐃𝐌𝐈𝐍 𝐋𝐈𝐒𝐓-𝐈 𝐘𝐄𝐍𝐈𝐃𝐄𝐍 𝐁𝐀𝐒𝐋𝐀𝐃𝐈𝐋𝐃𝐈 !"
    )


@Client.on_message(command(["pause", f"pause@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text(" Sɪʀᴀᴅᴀ Oxᴜɴᴀɴ ᴍᴜsɪǫɪ ʏᴏxᴅᴜʀ ᴍᴜsɪǫɪ ᴇʟᴀᴠᴇ ᴇᴛᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ /ᴘʟᴀʏ ᴍᴀʜɴɪ ᴀᴅɪ ʏᴀᴢ⚡")
    else:
        await callsmusic.pytgcalls.pause_stream(chat_id)
        await _.send_message(
            message.chat.id,
            "⏸ ᴏxᴜɴᴀɴ ᴍᴜsɪǫɪ ᴍᴜ̈ᴠᴇǫǫᴇᴛɪ ᴅᴀʏᴀɴᴅɪʀɪʟᴅɪ\n\n• ᴅᴀᴠᴀᴍ ᴇᴛᴅɪʀᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ✅\n» /resume ᴇᴍʀ-ɪɴɪ ɪşʟᴇᴅɪɴ."
        )


@Client.on_message(command(["resume", f"resume@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text(" ᴅᴀʏᴀɴᴅɪʀɪʟᴍɪş ᴍᴜsɪǫɪ ʏᴏxᴅᴜʀ ᴍᴜsɪǫɪ ᴇʟᴀᴠᴇ ᴇᴛᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ /ᴘʟᴀʏ✅")
    else:
        await callsmusic.pytgcalls.resume_stream(chat_id)
        await _.send_message(
            message.chat.id,
            "▶️ ᴍᴜsɪǫɪ ᴅᴀᴠᴀᴍ ᴇᴛᴅɪʀɪʟɪʀ.\n\n• ᴍᴜsɪǫɪɴɪ ᴍᴜ̈ᴠᴇǫǫᴇᴛɪ ᴅᴀʏᴀɴᴅɪʀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ \n» /pause ᴇᴍʀ-ɪɴɪ ɪşʟᴇᴅɪɴ."
        )


@Client.on_message(command(["end", f"end@{BOT_USERNAME}", "stop", f"end@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text(" ʙɪᴛɪʀᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ ᴍᴀʜɴɪ ʏᴏxᴅᴜʀ ᴍᴜsɪǫɪ ᴇʟᴀᴠᴇ ᴇᴛᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ /ᴘʟᴀʏ⚡")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass
        await callsmusic.pytgcalls.leave_group_call(chat_id)
        await _.send_message(
            message.chat.id,
            "✅ Oxᴜᴅᴜʟᴀɴ ᴍᴜsɪǫɪ ᴋᴇsɪʟᴅɪ ʏᴇɴɪᴅᴇɴ ᴍᴜsɪǫɪ ᴏxᴜᴅᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ /ᴘʟᴀʏ⚡"
        )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "next", f"next@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("ᴋᴇᴄ̧ᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ ᴍᴀʜɴɪ ʏᴏxᴅᴜʀ ᴍᴀʜɴɪ ᴇʟᴀᴠᴇ ᴇᴛᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ /ᴘʟᴀʏ⚡")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
                
    qeue = que.get(chat_id)
    if qeue:
        qeue.pop(0)
    if not qeue:
        return
    await _.send_message(
        message.chat.id,
        "⏭ ᴛᴏxᴜɴ've ʏᴇɴɪ ᴍᴀʜɴᴋʏᴀ ᴋᴇᴄ̧"
    )


@Client.on_message(command(["auth", f"auth@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        return await message.reply(" ʏᴇᴛᴋɪʟᴇɴᴅɪʀᴍᴇᴋ ɪsᴛᴇᴅɪʏɪɴɪᴢ ɪsᴛɪғᴀᴅᴇᴄ̧ɪʏᴇ ʏᴀɴɪᴛ ᴠᴇʀᴇʀᴇᴋ ɪşʟᴇᴛ🔥 !")
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply(
            "✅ ɪsᴛɪғᴀᴅᴇᴄ̧ɪ ᴀʀᴛɪɢ̆ ʏᴇᴛᴋɪʟɪᴅɪʀ\n\nᴏ ᴀᴅᴍɪɴ ʏᴇᴛᴋɪʟᴇʀɪɴᴅᴇɴ ɪsᴛɪғᴀᴅᴇ ᴇᴅᴇ ʙɪʟᴇʀ🤍."
        )
    else:
        await message.reply("✅ ɪsᴛɪғᴀᴅᴇᴄ̧ɪ ᴏɴsᴜᴢᴅᴀ ʏᴇᴛᴋɪʟɪᴅɪʀ")


@Client.on_message(command(["unauth", f"deauth@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        return await message.reply("ʏᴇᴛᴋɪsɪɴɪ ᴀʟᴀᴄᴀɢ̆ɪɴɪᴢ ɪsᴛɪғᴀᴅᴇᴄ̧ɪʏᴇ ʏᴀɴɪᴛ ᴏʟᴀʀᴀɢ̆ ʏᴀᴢɪɴ🔥 !")
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply(
            "❌ ɪsᴛɪғᴀᴅᴇᴄ̧ɪɴɪɴ ʏᴇᴛᴋɪsɪ ᴀʟɪɴᴅɪ.\n\n ᴏ ᴀʀᴛɪɢ̆ ʙᴏᴛᴜɴ ᴀᴅᴍɪɴ ᴇᴍʀʟᴇʀɪɴᴅᴇɴ ɪsᴛɪғᴀᴅᴇ ᴇᴅᴇ ʙɪʟᴍᴇʏᴇᴄᴇᴋ."
        )
    else:
        await message.reply("✅ ɪsᴛɪғᴀᴅᴇᴄ̧ɪɴɪɴ ᴏɴsᴜᴢᴅᴀ ʙᴏᴛᴅᴀ ʏᴇᴛᴋɪsɪ ʏᴏxᴅᴜʀ!")


# this is a anti cmd feature
@Client.on_message(command(["delcmd", f"delcmd@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def delcmdc(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            " /help ᴍᴇsᴀᴊɪ ᴏʟᴀʀᴀɢ̆ ɪşʟᴇᴅ"
        )
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "on":
        if await delcmd_is_on(message.chat.id):
            return await message.reply_text("✅ ᴏɴsᴜᴢᴅᴀ ᴀᴋᴛɪᴠᴅɪʀ")
        await delcmd_on(chat_id)
        await message.reply_text("✅ ᴀᴋᴛɪᴠ ᴇᴛᴍᴇ ᴜɢ̆ᴜʀʟᴜᴅᴜʀ")
    elif status == "off":
        await delcmd_off(chat_id)
        await message.reply_text("❌ ᴀᴋᴛɪᴠ ᴇᴛᴍᴇ sᴏ̈ɴᴅᴜ̈ʀᴜ̈ʟᴅᴜ̈")
    else:
        await message.reply_text(
            " /help ᴍᴇsᴀᴊɪ ᴏʟᴀʀᴀɢ̆ ɪşʟᴇᴅɪɴ"
        )


@Client.on_message(command(["volume", f"volume@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def change_volume(client, message):
    range = message.command[1]
    chat_id = message.chat.id
    try:
       await callsmusic.pytgcalls.change_volume_call(chat_id, volume=int(range))
       await message.reply(f"🔊 **ʜᴀᴢɪʀᴋɪ sᴇs sᴇᴠɪʏʏᴇsɪ:** ```{range}%```")
    except Exception as e:
       await message.reply(f"**error:** {e}")
