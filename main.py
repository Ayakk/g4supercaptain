import json
import hashlib
import requests
import time
import random

# API↓↓
public_key = '4948dd2ad64f8a47c7e882325121c4b2'
private_key = 'c8a4085bf1d97e3f1d3615f458986467ed40009a'
timestamp = str(time.time())  # pakt huidige tijd
hash_material = timestamp + private_key + public_key  # zet de tijd, private key en public key als 1 string
pre_hashed = hashlib.md5(hash_material.encode())  # bovenstaaande string converted to bytecode
hashed = pre_hashed.hexdigest()  # hier wordt de MD5 hash gegenereerd
character_random_interval = str(random.randint(100, 1000))  # zorgt ervoor dat de set gekozen characters random blijven
character_limit = "100"
param = {"ts": timestamp, #wat de Marvel server vereist om te functioneren
         'apikey': '4948dd2ad64f8a47c7e882325121c4b2', #public_key
         "hash": hashed,
         "limit": character_limit,
         "offset": character_random_interval
         }

def getMarvelCharacter():  # maakt verbinding met de marvel server en haalt een aantal superheroes op. pakt 1 random superhero met de criteria "has description"
    url = 'https://gateway.marvel.com:443/v1/public/characters'
    response = requests.get(url, params=param)
    response = response.json()
    text = json.dumps(response, indent=4) #formateerd text om in een bestand op te slaan
    with open('characters.txt', 'w+') as f:
        f.write(text)
    with open('characters.txt', 'r') as f:
        text = json.load(f) #Haalt data op voor gebruik in programma
    teller = 0
    begin_character_lijst = []
    alle_character_lijst = []
    einde_character_lijst = []

    for i in range(9):
        alle_character_lijst.append(text["data"]["results"][random.randint(0, 50)])

    for i in text["data"]["results"]: #maakt een dictionary met gegevens van het juiste character op
        if len(text["data"]["results"][teller]["description"]) > 2:
            begin_character_lijst.append(text["data"]["results"][teller])
        teller += 1
    einde_character_lijst.append(begin_character_lijst[random.randint(0, (len(begin_character_lijst) - 1))])
    return einde_character_lijst, alle_character_lijst
# API↑↑

def getMarvelCharacterHint(character_lijst):  # splits de description in delen aan de hand van comma's
    character_hint = character_lijst[0]["description"]
    character_hint = character_hint.split(",")
    return character_hint


def goed():
    global punten
    global totaal_punten
    totaal_punten += punten
    punten = 25
    return totaal_punten


def fout():
    global punten
    if punten <= 0:
        punten = 0
        return punten
    else:
        punten -= 1
        return punten


def highscorefile():
    highscore = open("SuperGuesserHighscore.txt", "a")
    highscore.write(speler_naam)
    highscore.write(": ")
    highscore.write(str(punten))
    highscore.write("\n")


def hint_geven():
    global punten
    global character_hints
    if len(character_hints) == 0:
        print("Er zijn geen hints meer. U moet een gokje wagen")
        return 0
    elif punten <= 3:
        print('U heeft te weinig punten om een hint te vragen. U moet een gokje wagen\n')
        return 0
    else:
        print(character_hints[0])
        character_hints.pop(0)
        punten -= 3
    print("Jouw score : {}".format(punten))
    while True:
        aanvraag_hint = input("Wilt u nog een hint? ja of nee\n")
        if aanvraag_hint not in "jahint":
            break
        elif punten <= 3:
            print('U heeft te weinig punten om een hint te vragen. U moet een gokje wagen')
            break
        elif len(character_hints) == 0:
            print("Er zijn geen hints meer. U moet een gokje wagen")
            break
        else:
            print(character_hints[0])
            character_hints.pop(0)
            punten -= 3
            print("Jouw score : {}".format(punten))

#------------------------------------------------------Hier begint het programma-------------------------

all_character_info = getMarvelCharacter() # haalt 2 lijsten op, eentje met de juiste hero en eentje met 9 random
all_wrong_character_info = all_character_info[1] #haalt een lijst op van dictionaries met character informatie
wrong_character_info = []
for i in range((len(all_wrong_character_info))): #haalt alleen de namen op van alle random characters
    if all_wrong_character_info[i]["name"] not in wrong_character_info:
        wrong_character_info.append(all_wrong_character_info[i]["name"])
right_character_info = list(all_character_info[0])#haalt de informatie op van de superhero
character_name = right_character_info[0]["name"] # dit is de naam va de superhero
print(character_name)  # Voor testen
wrong_character_info.append(character_name) # zet de naam van de superhero in de lijst met random
random.shuffle(wrong_character_info) # haalt alle namen door elkaar anders staat de juiste naam altijd onderaan
print(wrong_character_info) # Voor testen

if type(character_name) == 'list':
    character_name = character_name[0]

character_hints = getMarvelCharacterHint(right_character_info) #haalt hints op van de superhero
verwijder_name_hint = ""
for i in range(0,len(character_hints)): #haalt de naam van de superhero uit de hint
    if character_name in character_hints[i]:
        character_hints[i] = character_hints[i].replace(character_name, "Hero")

#----------------Hier begint de spel--------------------------------
punten = 25
totaal_punten = 0

while True:
    speler_naam = input("Wat is jouw naam? ")
    if len(speler_naam) >= 2:
        break
    print("Naam niet lang genoeg")
print(character_name)
print("Jouw eerste hint(gratis):" + character_hints[0])
character_hints.pop(0)
while punten > 0:
    antwoord = input("Welke superheld is het?")
    if antwoord == "hint":
        hint_geven()
    elif antwoord != character_name:
        fout()
        print("Jouw score : {}".format(punten))
    elif antwoord == character_name:
        print("Gefeliciteerd, je antwoord is correct!")
        print("Jouw score : {}".format(punten))
        highscorefile()
        break

if punten == 0:
    print('Helaas je hebt verloren.')
    highscorefile()
