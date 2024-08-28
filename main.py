import requests
import customtkinter
import tkinter
from dotenv import load_dotenv
import os
import json

load_dotenv()
api_server = 'https://api.serverseeker.net'
get = requests.get
post = requests.post

#Set API key
apikey = os.getenv("API_KEY")

def getrandomserver(api_key):
    req = post(f'{api_server}/servers',json={'api_key': api_key})
    server = json.loads(req.text)
    print(json.dumps(server, indent=4, sort_keys=True))

    with open('servers.json', 'w+') as outfile:
        outfile.write(json.dumps(server, indent=4, sort_keys=True))

def format_dict(d, prefix=""):
    lines = []
    for key, value in d.items():
        if isinstance(value, dict):
            lines.extend(format_dict(value, prefix=f"{prefix}{key}."))
        else:
            lines.append(f"{prefix}{key}: {value}")
    return lines

getrandomserver(apikey)