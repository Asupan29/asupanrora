# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL1, FORCE_SUB_GROUP1, FORCE_SUB_CHANNEL2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Help", callback_data="help"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Help", callback_data="help"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Help", callback_data="help"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL1 and FORCE_SUB_GROUP1 and FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="Help", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink),
                InlineKeyboardButton(text="JOIN", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink3),
                InlineKeyboardButton(text="JOIN", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink5),
            ],
            [InlineKeyboardButton(text="Close", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons


    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL1 and FORCE_SUB_GROUP1 and FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink),
                InlineKeyboardButton(text="JOIN", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink3),
                InlineKeyboardButton(text="JOIN", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="JOIN", url=client.invitelink5),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
