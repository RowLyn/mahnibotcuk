"""
MIT License
Copyright (C) 2021 KennedyXMusic
This file is part of https://github.com/KennedyProject/KennedyXMusic
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from KennedyMusic.callsmusic.callsmusic import client as USER
from KennedyMusic.config import BOT_USERNAME, SUDO_USERS
from KennedyMusic.helpers.decorators import authorized_users_only, errors
from KennedyMusic.helpers.filters import command


@Client.on_message(command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text("<b>ᴍᴇɴɪ ᴀᴅᴍɪɴ ᴇᴛ !</b>")
        await message.reply_sticker("CAACAgUAAx0CYPNCJwACJpthfoPdqrvoutRwQzk_v9bqUyOnugACRgADE_yaMj3RPONrfXfZIQQ")
        return
    try:
        user = await USER.get_me()
    except:
        user.first_name = "music assistant"
    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤖: ᴍᴇɴ ᴍᴜsɪǫɪ ᴏxᴜᴅᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ ɢᴇʟᴅɪᴍ")
        await USER.send_sticker(message.chat.id, "CAACAgUAAx0CYPNCJwACJpdhfoO6uBuC9b2EglpYeiNKOMtqJAACNQADE_yaMk-0JIP096z2IQQ")
    except UserAlreadyParticipant:
        await message.reply_text(f"<b>✅ ᴀsɪsᴛᴀɴ ᴏɴsᴜᴢᴅᴀ ɢʀᴜʙᴅᴀᴅɪʀ</b>")
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait xᴇᴛᴀsɪ 🛑 \n\n ɪsᴛɪғᴀᴅᴇᴄ̧ɪ {user.first_name}  ɢʀᴜʙᴀ ǫᴀᴛɪʟᴍᴀ ɪsᴛᴇʏɪ ᴄ̧ᴏx ᴏʟᴅᴜɢ̆ᴜɴᴅᴀɴ ᴀsɪsᴛᴀɴ ɢʀᴜʙᴀ ǫᴀᴛɪʟᴀ ʙɪʟᴍᴇᴅɪ."
            "\n\nOɴᴜ ᴇʟɪɴʟᴇ ɢʀᴜʙᴀ ᴇʟᴀᴠᴇ ᴇᴛ</b>",
        )
        return
    await message.reply_text(f"<b>✅ ᴀsɪsᴛᴀɴ ᴜɢ̆ᴜʀʟᴀ ɢʀᴜʙᴀ ᴇʟᴀᴠᴇ ᴏʟᴜɴᴅᴜ</b>")


@Client.on_message(command(["userbotleave", f"userbotleave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def rem(client, message):
    try:
        await USER.send_sticker(message.chat.id, "CAACAgUAAx0CYPNCJwACA0RhbkLHaItFAAFFSUQZW3YhLiqJb2MAAgYFAAIclOFWYPPBpmhRMYUhBA")
        await USER.send_message(message.chat.id, "✅ ᴍᴇɴ ɢʀᴜʙᴅᴀɴ ᴀʏʀɪʟɪʀᴀᴍ, ᴜɢ̆ᴜʀʟᴀʀ!")
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text("<b>ᴀsɪsᴛᴀɴ ᴀʏʀɪʟᴀ ʙɪʟᴍᴇᴅɪ ᴏɴᴜ ᴇʟɪɴʟᴇ ᴄ̧ɪxᴀʀ</b>")
        return


@Client.on_message(command(["userbotleaveall", f"userbotleaveall@{BOT_USERNAME}"]))
async def bye(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("Assistant Leaving all chats")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"ᴀsɪsᴛᴀɴ ʙᴜ̈ᴛᴜ̈ɴ ɢʀᴜʙʟᴀʀᴅᴀɴ ᴀʏʀɪʟɪʀ... \n\nLeft: {left} chats. Failed: {failed} chats."
            )
        except:
            failed += 1
            await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
        await asyncio.sleep(0.7)
    await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
