#!/usr/local/bin/python3
#HTB_invitecode.py 
import requests
import random
import json
import base64

"""By HtetPaing"""          

url = "https://www.hackthebox.eu/api/invite/generate"
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',]
user_agent = random.choice(user_agent_list)
headers = {"User-Agent" : user_agent}
req = requests.post(url,headers=headers)
dict = json.loads(req.text)
code = dict['data']['code']
print((base64.b64decode(code)).decode())
