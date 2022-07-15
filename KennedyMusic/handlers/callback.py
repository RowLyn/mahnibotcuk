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


from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from KennedyMusic.helpers.decorators import authorized_users_only
from KennedyMusic.config import BOT_NAME as bn, BOT_IMG, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME, UPSTREAM_REPO
from KennedyMusic.handlers.play import cb_admin_check


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> 𝐒𝐀𝐋𝐀𝐌 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})!</b>

**💭 [{bn}](https://t.me/{GROUP_SUPPORT}) 𝐊𝐎𝐌𝐄𝐊 𝐋𝐀𝐙𝐈𝐌 𝐎𝐋𝐀𝐑𝐒𝐀 𝐒𝐔𝐏𝐏𝐎𝐑𝐓𝐀 𝐁𝐔𝐘𝐔𝐑𝐔𝐍!**

📡 𝐁𝐎𝐓𝐔𝐍 𝐁𝐔𝐓𝐔𝐍 𝐄𝐌𝐑𝐋𝐄𝐑𝐈 𝐔𝐂̧𝐔𝐍 **» ⚙️ 𝐄𝐌𝐑** 𝐓𝐎𝐗𝐔𝐍!""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ 𝐌𝐄𝐍𝐈 𝐆𝐑𝐔𝐁𝐀 𝐄𝐋𝐀𝐕𝐄 𝐄𝐓 ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "⚙️ 𝐄𝐌𝐑𝐋𝐄𝐑", callback_data="cbhelp"
                    ),
                    InlineKeyboardButton(
                        "❤️ 𝐊𝐎𝐌𝐄𝐊", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "⚜️𝐃𝐄𝐒𝐓𝐄𝐊 𝐆𝐑𝐔𝐁𝐔", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿𝐑𝐄𝐒𝐌𝐈 𝐊𝐀𝐍𝐀𝐋", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "🛠️ 𝐑𝐄𝐏𝐎🍷 🛠️", url=f"{UPSTREAM_REPO}")
                ],[
                    InlineKeyboardButton(
                        "❔ 𝐇𝐀𝐐𝐐𝐈𝐌𝐃𝐀​​", callback_data="cbabout"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbabout"))
async def cbabout(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>❓ **𝐇𝐀𝐐𝐐𝐈𝐌𝐃𝐀 {bn}**</b> 

➠ **𝐒𝐄𝐒𝐋𝐈 𝐒𝐎𝐇𝐁𝐄𝐓𝐋𝐄𝐑𝐃𝐄 𝐌𝐔𝐒𝐈𝐐𝐈 𝐎𝐗𝐔𝐃𝐌𝐀𝐆 𝐔𝐂̧𝐔𝐍 𝐘𝐀𝐑𝐀𝐃𝐈𝐋𝐌𝐈𝐒̧𝐀𝐌!

➠ 𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌 𝐃𝐈𝐋𝐈𝐍𝐃𝐄 𝐊𝐎𝐃𝐋𝐀𝐍𝐌𝐀😴

➠ 𝐈̇𝐒𝐓𝐈̇𝐅𝐀𝐃𝐄 𝐎𝐋𝐔𝐍𝐀𝐍 𝐏𝐘𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐘𝐀𝐒𝐈 3.9.7

➠ 𝐘𝐎𝐔𝐓𝐔𝐁𝐄𝐃𝐀𝐍 𝐌𝐀𝐇𝐍𝐈 𝐘𝐔𝐊𝐋𝐄𝐌𝐄𝐊 𝐕𝐄𝐘𝐀 𝐌𝐀𝐇𝐍𝐈𝐘𝐀 𝐐𝐔𝐋𝐀𝐆̆ 𝐀𝐒𝐌𝐀𝐆

__{bn} licensed under the GNU General Public License v.3.0__

• Updates channel @{UPDATES_CHANNEL}
• Group Support @{GROUP_SUPPORT}
• Assistant @{ASSISTANT_NAME}
• Here is my [Owner](https://t.me/{OWNER_NAME})**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri​", callback_data="cbstart"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🎛️ ʙᴜʀᴀ ᴋᴏ̈ᴍᴇᴋ ᴍᴇɴʏᴜsᴜᴅᴜʀ !</b>

**ʙᴏᴛᴜɴ ʙᴜᴛᴜɴ ᴇᴍʀʟᴇʀɪ ᴀşᴀɢ̆ɪᴅᴀᴅɪʀ**

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠️ ɪsᴛɪғᴀᴅᴇᴄ̧ɪ ᴇᴍʀʟᴇʀɪ", callback_data="cbbasic"),
                    InlineKeyboardButton(
                        "👮 ᴀᴅᴍɪɴ ᴇᴍʀʟᴇʀɪ", callback_data="cbadmin"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👷 sᴜᴅᴏ ᴇᴍʀʟᴇʀɪ", callback_data="cbsudo"),
                    InlineKeyboardButton(
                        "🤴 ᴏᴡɴᴇʀ", callback_data="cbowner"
                    ) 
                ],
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🛠️ ʙᴏᴛᴜɴ ɪsᴛɪғᴀᴅᴇᴄ̧ɪʟᴇʀ ᴍᴇɴʏᴜsᴜ

[GROUP SETTINGS]
 • `/play (ᴀᴅ / ᴠᴇ ʏᴀ ᴍᴜsɪǫɪʏᴇ ʏᴀɴɪᴛ ᴏʟᴀʀᴀɢ̆)` - ᴍᴜsɪǫɪ ᴏxᴜᴅᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ
 • `/ytp (ᴀᴅ)` - ᴄᴀɴʟɪ ᴍᴜsɪǫɪ ᴏxᴜᴅᴀʀ
 • `/playlist` - ᴘʟᴀʏʟɪsᴛ ᴀxᴛᴀʀᴀʀ
 • `/song (ᴀᴅ)` - ᴍᴜsɪǫɪɴɪ ʏᴜ̈ᴋʟᴇʏᴇʀ
 • `/search (ᴀᴅ)` - ᴍᴜsɪǫɪ ᴅᴇᴛᴀʟʟᴀʀɪɴɪ ᴀxᴛᴀʀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ
 • `/video (ᴀᴅ)` - ᴠɪᴅᴇᴏ ʏᴜ̈ᴋʟᴇʏᴇʀ
[ MORE ]
 • `/alive` - ʙᴏᴛᴜɴ ɪşʟᴇᴅɪʏɪ ʜᴀǫǫɪɴᴅᴀ ᴍᴇʟᴜᴍᴀᴛ
 • `/start` - ʙᴏᴛᴜ ʙᴀşʟᴀᴅᴀʀ

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>👮 ᴀᴅᴍɪɴ ᴇᴍʀʟᴇʀɪ!

 • `/player` - ᴍᴜsɪǫɪ ᴏxᴜᴅᴜᴄᴜ
 • `/pause` - ᴍᴜsɪǫɪɴɪ ᴍᴜ̈ᴠᴇǫǫᴇᴛɪ ᴅᴀʏᴀɴᴅɪʀᴀʀ
 • `/resume` - ᴅᴀʏᴀɴᴅɪʀɪʟᴍɪş ᴍᴜsɪǫɪɴɪ ᴅᴀᴠᴀᴍ ᴇᴛᴅɪʀᴇʀ
 • `/skip` - ᴍᴜsɪǫɪɴɪ ᴋᴇᴄ̧ᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ
 • `/end` - ᴍᴜsɪǫɪɴɪ ᴅᴀʏᴀɴᴅɪʀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ
 • `/userbotjoin` - ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴇᴠᴇᴛ ᴇᴛᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ
 • `/musicp (on / off)` - ᴍᴜsɪǫɪ ᴏxᴜᴅᴜᴄᴜʏᴜ ʏᴀɴᴅɪʀᴍᴀɢ̆ ᴠᴇ ʏᴀ sᴏ̈ɴᴅᴜ̈ʀᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**🤴 ʏᴀʀᴀᴅɪᴄɪ ᴇᴍʀʟᴇʀɪ**

 • `/stats` - ʙᴏᴛ sᴛᴀᴛɪsᴛɪᴋᴀsɪɴɪ ɢᴏ̈sᴛᴇʀᴇʀ
 • `/broadcast` (ʏᴀɴɪᴛ ᴏʟᴀʀᴀɢ̆) - ʙᴏᴛʟᴀ ᴍᴇsᴀᴊ ɢᴏ̈ɴᴅᴇʀᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ
 • `/block` ( id - ᴛᴀɢ - ᴠᴇ ʏᴀ ᴍᴇsᴀᴊᴀ ʏᴀɴɪᴛ ᴏʟᴀʀᴀɢ̆) - ʙʟᴏᴋʟᴀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ
 • `/unblock` ( id - ᴛᴀɢ - ᴠᴇ ʏᴀ ᴍᴇsᴀᴊᴀ ʏᴀɴɪᴛ ᴏʟᴀʀᴀɢ̆) - ʙʟᴏᴋᴅᴀɴ ᴄ̧ɪxᴀʀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ
 • `/blocklist` - ʙᴏᴛʟᴀ ʙʟᴏᴋʟᴀɴᴀɴʟᴀʀɪɴ ʟɪsᴛ ɪɴɪ ɢᴏ̈sᴛᴇʀᴇʀ

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri Gel", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>👷 **sᴜᴅᴏ ᴇᴍʀʟᴇʀɪ**

 • `/userbotleaveall - ᴀsɪsᴛᴀɴɪ ʙᴜ̈ᴛᴜ̈ɴ ɢʀᴜʙʟᴀʀᴅᴀɴ ᴄ̧ɪxᴀʀᴅᴀʀ
 • `/gcast` - ᴀsɪsᴛᴀɴʟᴀ ᴍᴇsᴀᴊ ᴀᴛᴀʀ
 • `/rmd` - ʏᴜ̈ᴋʟᴇɴɪʟᴇɴ ғᴀʏʟɪ sɪʟᴇʀ
 • `/uptime` - sᴛᴀʀᴛ ᴢᴀᴍᴀɴɪ ᴀʏᴀʀʟᴀʀɪ ɢᴏ̈ʀ
 • `/sysinfo` - ʙᴏᴛ sɪsᴛᴇᴍɪ ʜᴀǫǫɪɴᴅᴀ ᴍᴇʟᴜᴍᴀᴛ ᴠᴇʀᴡʀ
 • `/eval` (cmd) and `/sh` (cmd) - ᴄᴍᴅ ɴɪ ᴄ̧ᴀʟɪşᴅɪʀᴀʀ
 • `/usage` - ʜᴇʀᴏᴋᴜᴅᴀ ɴᴇᴄ̧ᴇ sᴀᴀᴛ ᴅʏɴᴏ ǫᴀʟᴅɪɢ̆ɪɴɪ ɢᴏ̈sᴛᴇʀᴇʀ
 • `/update` - ʙᴏᴛᴜ ɢᴜ̈ɴᴄᴇʟʟᴇʏᴇʀ
 • `/restart` - ʙᴏᴛᴜ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴅᴀʀ
 • `/setvar` (var) (value) - ʜᴇʀᴏᴋᴜᴅᴀᴋɪ ᴠᴀʟᴜᴇ ʟᴀʀɪ ᴅᴇʏɪşᴇʀ
 • `/delvar` (var) - ʜᴇʀᴏᴋᴜᴅᴀᴋɪ ᴠᴀʟᴜᴇ ʟᴇʀɪ sɪʟᴇʀ.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ʙᴏᴛ ɴᴇᴄᴇ ɪşʟᴇᴅɪʟᴇʀ :**

1.) Mᴇɴɪ ɢʀᴜʙᴀ ᴇʟᴀᴠᴇ ᴇᴛ
2.) Mᴇɴɪ ᴀᴅᴍɪɴ ᴇᴛ
3.) Asɪsᴛᴀɴɪ ʀʟᴀᴠᴇ ᴇᴛ ɢʀᴜʙᴀ@{ASSISTANT_NAME} ᴏʟᴍᴀᴢsᴀ `/userbotjoin` ʙᴜɴʟᴀ ᴅᴇᴠᴇᴛ ᴇᴛ.
4.) sᴇsʟɪ sᴏ̈ʜʙᴇᴛ ᴀᴄ̧ ᴠᴇ ᴍᴀʜɴɪʏᴀ ǫᴜʟᴀɢ̆ ᴀs.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗑 Çıx", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbhplay"))
async def cbhplay(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""💭 ʙᴏᴛ ɴᴇᴄᴇ ɪşʟᴇᴅɪʟɪʀ {bn}

• `/play (ᴀxᴛᴀʀ ᴠᴇ ʏᴀ ᴍᴀʜɴɪʏᴀ ʏᴀɴɪᴛ ᴠᴇʀ)` - ᴠᴇ ᴍᴀʜɴɪɴɪ ᴏxᴜᴅ
• `/ytp (ᴀxᴛᴀʀ)` - ʏᴏᴜᴛᴜʙᴇ ᴅᴀɴ ᴍᴀʜɴɪʏᴀ ǫᴜʟᴀɢ̆ ᴀsᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ

🔔 ʀᴇsᴍɪ ᴋᴀɴᴀʟ [Click here](https://t.me/{UPDATES_CHANNEL})""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton("🔙 Geri", callback_data="cbplayback"),
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbplayback"))
async def cbplayback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**❗ ɴᴇ ʙɪʟɪᴍ **

» **please provide the correct song name or include the artist's name as well**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton("𝐄𝐌𝐑", callback_data="cbhplay"),
                ],
                [
                   InlineKeyboardButton("🗑️ çıx", callback_data="closed"),
                ],
            ]
        ),
    )
