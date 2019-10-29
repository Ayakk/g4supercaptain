import json
import hashlib
import requests
import time
import random
#Dit maakt verbinding met de Marvel server om informatie op te halen

public_key = '4948dd2ad64f8a47c7e882325121c4b2'
private_key = 'c8a4085bf1d97e3f1d3615f458986467ed40009a'
timestamp = str(time.time()) # pakt huidige tijd
hash_material = timestamp+private_key+public_key #zet de tijd, private key en public key als 1 string
pre_hashed = hashlib.md5(hash_material.encode()) #bovenstaaande string converted to bytecode
hashed = pre_hashed.hexdigest()# hier wordt de MD5 hash gegenereerd
character_random_interval = str(random.randint(2, 30)) #zorgt ervoor dat de set gekozen characters random blijven
character_limit = "10"
param = {"ts": timestamp,
         'apikey': '4948dd2ad64f8a47c7e882325121c4b2',
         "hash": hashed,
         "limit": character_limit,
         "offset": character_random_interval
         }
#hash - a md5 digest of the ts parameter, your private key and your public key (e.g. md5(ts+privateKey+publicKey)

#voorbeeld link  http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def getMarvelCharacters():
    characters = []
    url = 'https://gateway.marvel.com:443/v1/public/characters'
    response = requests.get(url, params=param)
    response = response.json()
    text = json.dumps(response, indent=4)
    # voor controle
    with open('characters.txt', 'w+') as f:
        f.write(text)
    print(text)


print(getMarvelCharacters())
