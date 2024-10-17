from b3_gate import Tele
from hit_sender import hit, die
import random
import time
import concurrent.futures
import os
from colorama import Fore, Style
import telebot
from telebot import types

sto = {"stop": False}
token = "7519672194:AAEiBXdvy_D4mNLQrUhGkEAttmowetGHhRs"
admin_id = 6930293729  # Admin ID
authorized_users = [admin_id]  # Initially only the admin is authorized
bot = telebot.TeleBot(token, parse_mode="HTML")

def incorrect(cc):
    with open('ccn.txt', "a") as file:
        file.write(cc + '\n')

def newres(cc):
    with open('newres.txt', "a") as file:
        file.write(cc + '\n')

@bot.message_handler(commands=["start"])
def start(message):
    if message.from_user.id in authorized_users:
        bot.reply_to(message, "❤‍🩹 𝐇𝐞𝐲 𝐍𝐢𝐠𝐠𝐚 ! 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐓𝐡𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 combo.txt 𝐅𝐢𝐥𝐞 𝐅𝐨𝐫 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐂𝐚𝐫𝐝𝐬.")
        sto.update({"stop": False})
    else:
        bot.reply_to(message, "You are not authorized to use this bot.")

@bot.message_handler(commands=["addu"])
def add_user(message):
    if message.from_user.id == admin_id:
        try:
            user_id = int(message.text.split()[1])
            if user_id not in authorized_users:
                authorized_users.append(user_id)
                bot.reply_to(message, f"User {user_id} has been added to authorized users.")
            else:
                bot.reply_to(message, f"User {user_id} is already authorized.")
        except (IndexError, ValueError):
            bot.reply_to(message, "Please provide a valid Telegram user ID after /addu.")
    else:
        bot.reply_to(message, "You are not authorized to add users.")

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_callback(call):
    if call.from_user.id in authorized_users:
        sto.update({"stop": True})
        bot.answer_callback_query(call.id, text='Stopping Bot. Please Wait 10 seconds')
    else:
        bot.answer_callback_query(call.id, text="You are not authorized to stop this bot.")

@bot.message_handler(content_types=["document"])
def main(message):
    if sto["stop"]:
        bot.reply_to(message, "Bot is stopped. Restart with /start.")
    elif message.from_user.id in authorized_users:
        main_process(message)
    else:
        bot.reply_to(message, "You are not authorized to use this bot.")

def main_process(message):
    username = message.from_user.username
    chat_id = message.from_user.id
    file_name = "combo.txt"
    folder_name = str(message.from_user.id)
    folder_path = os.path.join(os.getcwd(), folder_name)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    dd, ccn, ch = 0, 0, 0
    res = '...'
    ko = bot.send_message(chat_id, "⌛𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐚𝐫𝐝𝐬....... ")
    file_info = bot.get_file(message.document.file_id)
    ee = bot.download_file(file_info.file_path)
    with open(file_path, "wb") as w:
        w.write(ee)

    try:
        with open(file_path, 'r') as file:
            lino = file.readlines()
            total = len(lino)
            for cc in lino:
                if sto["stop"]:
                    bot.send_message(chat_id=chat_id, text="Stopped Bot.")
                    break
                
                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f" {cc} ", callback_data='u8')
                cm0 = types.InlineKeyboardButton(f"{res}", callback_data='x')
                cm2 = types.InlineKeyboardButton(f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ : {ch}  ", callback_data='x')
                cm4 = types.InlineKeyboardButton(f"𝐂𝐂𝐍 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ♻️:  {ccn} ", callback_data='x')
                cm5 = types.InlineKeyboardButton(f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌  : {dd} ", callback_data='x')
                cm6 = types.InlineKeyboardButton(f"💳 𝐓𝐨𝐭𝐚𝐥 𝐂𝐚𝐫𝐝𝐬 : {total} ", callback_data='x')
                stop_button = types.InlineKeyboardButton("🔕 𝐒𝐭𝐨𝐩 𝐒𝐞𝐬𝐬𝐢𝐨𝐧", callback_data='stop')
                mes.add(cm0, cm1, cm2, cm4, cm5, cm6, stop_button)
                bot.edit_message_text(chat_id=chat_id, message_id=ko.message_id, text="♻️ 𝐀𝐡𝐡 𝐍𝐢𝐠𝐠𝐚!\n\n𝐈 𝐇𝐚𝐯𝐞 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐚𝐫𝐝𝐬. \n\n❤️‍🩹 𝐁𝐨𝐭 𝐁𝐲 : @Ishowchhetri [🇳🇵]", reply_markup=mes)
                
                ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
                time.sleep(4)
                
                def check_gateway(gateway):
                    try:
                        result2 = str(gateway(cc))
                        return result2
                    except Exception as e:
                        return str(e)
                
                gateways = [Tele]
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    results = list(executor.map(check_gateway, gateways))
  
                for gateway, result2 in zip(gateways, results):
                    gate = "Braintree"
                    amt = "Auth"
                    result2 = result2.lower()

                    success_keys = ["1000:Approved ✅", "1000:approved ✅"]
                    ccn_approved_keys = ["CCN Approved ✅", "ccn approved ✅"]
                    failure_keys = ["Declined ❌", "declined ❌"]
                    found_match = False

                    for key in success_keys:
                        if key in result2:
                            print(Fore.GREEN + f"{key} {gate} {cc}" + Style.RESET_ALL)
                            found_match = True
                            res = f"{key}"
                            ch += 1
                            #send(amt, cc, ip_address, gate, key, chat_id)
                            hit(amt, cc, gate, key, username, chat_id)
                            break

                    for key in failure_keys:
                        if key in result2:
                            print(Fore.RED + f"{key} {gate} {cc}" + Style.RESET_ALL)
                            found_match = True
                            res = f"{key}"
                            dd += 1
                            break

                    for key in ccn_approved_keys:
                        if key in result2:
                            print(Fore.MAGENTA + f"{key} {gate} {cc}" + Style.RESET_ALL)
                            found_match = True
                            res = f"{key}"
                            ccn += 1
                            incorrect(cc)
                            hit(amt, cc, gate, key, username, chat_id)
                            break

                    if not found_match:
                        print(Fore.YELLOW + f"Unknown Response: {result2}" + Style.RESET_ALL)
    except Exception as e:
        print(f"Error: {e}")

print("Bot is working")
bot.polling()
