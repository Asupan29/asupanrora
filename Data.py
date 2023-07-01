from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
 Perintah untuk Pengguna BOT
  /start - Mulai Bot
  /about - Tentang Bot ini
  /help - Bantuan Perintah Bot ini
  /ping - Untuk mengecek bot hidup
  /uptime - Untuk melihat status bot 
 
 Perintah Untuk Admin BOT
  /logs - Untuk melihat logs bot
  /setvar - Untuk mengatur var dengan command dibot
  /delvar - Untuk menghapus var dengan command dibot
  /getvar - Untuk melihat salah satu var dengan command dibot
  /users - Untuk melihat statistik pengguna bot
  /batch - Untuk membuat link lebih dari satu file
  /speedtest - Untuk Mengetes kecepatan server bot
  /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

Develoved by @saya_wiki
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    ABOUT = """
Saya Bot Asupan.

 • Owner: @saya_wiki
 • Group: https://t.me/+ko7-P2yUhkgyODQx
 • Channel: https://t.me/+VlNr5lgAgNExOWM5
"""
