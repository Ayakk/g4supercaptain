import json
import hashlib
import requests
import time
import random
from tkinter import *
from tkinter.ttk import *





#Dit maakt verbinding met de Marvel server om informatie op te halen

public_key = '4948dd2ad64f8a47c7e882325121c4b2'
private_key = 'c8a4085bf1d97e3f1d3615f458986467ed40009a'
timestamp = str(time.time()) # pakt huidige tijd
hash_material = timestamp+private_key+public_key #zet de tijd, private key en public key als 1 string
pre_hashed = hashlib.md5(hash_material.encode()) #bovenstaaande string converted to bytecode
hashed = pre_hashed.hexdigest()# hier wordt de MD5 hash gegenereerd
character_random_interval = str(random.randint(100, 500)) #zorgt ervoor dat de set gekozen characters random blijven
character_limit = "100"
param = {"ts": timestamp,
         'apikey': '4948dd2ad64f8a47c7e882325121c4b2',
         "hash": hashed,
         "limit": character_limit,
         "offset": character_random_interval
         }

#hash - a md5 digest of the ts parameter, your private key and your public key (e.g. md5(ts+privateKey+publicKey)

#API↓↓

def getMarvelCharacter():#maakt verbinding met de marvel server en haalt een aantal superheroes op
    url = 'https://gateway.marvel.com:443/v1/public/characters'
    response = requests.get(url, params=param)
    response = response.json()
    text = json.dumps(response, indent=4)
    with open('characters.txt', 'w+') as f:
        f.write(text)
    with open('characters.txt','r') as f:
        text = json.load(f)
    teller = 0
    begin_character_lijst = []
    einde_character_lijst = []

    for i in text["data"]["results"]:
        if text["data"]["results"][teller]["description"] != "":
            begin_character_lijst.append(text["data"]["results"][teller])
        teller += 1

    einde_character_lijst.append(begin_character_lijst[random.randint(0, (len(begin_character_lijst) - 1))])
    return einde_character_lijst

def getMarvelCharacterHint(character_lijst): #pakt 1 random superheroe met de criteria "has description"
    character_hint = character_lijst[0]["description"]

#API↑↑

punten = 25
totaal_punten = 0

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

def hint():
    global punten
    if punten < 3:
        return print('Je hebt niet genoeg punten')
    else:
        punten -= 3
        return punten

def highscorefile():
    highscore = open("SuperGuesserHighscore.txt", "a")
    highscore.write(speler_naam)
    highscore.write(": ")
    highscore.write(str(punten))
    highscore.write("\n")


character_info = getMarvelCharacter()
character_names = character_info[0]["name"].split('/') #voorkomt dat de menselijke naam van de superheroe ook met de superhero naam komt (bijv.Clark Kent)
character_name = character_names[0]

getMarvelCharacterHint(character_info)


#Vraagt naar naam van speler
while True:
    speler_naam = input("Wat is jouw naam? ")
    if len(speler_naam) >= 2:
        break
    print("Naam niet lang genoeg")
while punten > 0:
        antwoord = input("Welke superheld is het?")
        #eerste hint hoort hier (Daniel en Frank)

        if antwoord != "jan":
            fout()
            print("Jouw score : {}".format(punten))

        elif antwoord == "jan":
            print("Gefeliciteerd, je antwoord is correct!")
            highscorefile()
            break

if punten == 0:
    print('Helaas je hebt verloren.')
    highscorefile()


speler_naam_lijst = [speler_naam]

gui = Tk()
gui.title("SuperGuesser")
gui.geometry("1000x750")

punten = 25

scoredict = {}



pakNaam = input("Wat is je username? ")

# def pakNaam():
#     username_entry = naaminput.get()
#     stringvoorlabel = "Uw naam is " + username_entry
#     labelusername = Label(gui,text=stringvoorlabel, font="Arial 12 bold")
#     labelusername.place(x=40, y=700)
#
# #GEEF JE NAAM
# naaminput = Entry(gui, text="Voer je username in ").place(x=500, y=500)
# naambutton = Button(gui, text="Voer in", command=pakNaam()).place(x=600, y=500)

#MAAK DE WIDGETS
score = Label(gui, text="Je hebt " + str(punten) + " punten!", font="Arial 12").place(x=0, y=0)
tot_score = Label(gui, text="Je hebt in totaal " + str(punten) + " punten!", font="Arial 12").place(x=0, y=20)
username = Label(gui, text="Jouw gebruikersnaam is: "+pakNaam, font="Arial 12 italic").place(x=0, y=40)
hints = Label(gui, text="HINTLIJST:", font="Arial 12 bold").place(x=350, y=200)
inhoudHintlijst = Label(gui, text="Inhoud", font="Arial 12 italic").place(x=350, y=250)
def leesNaam():
    f = open('SuperGuesserHighscore.txt', "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    str(lines).replace('[', '')
    str(lines).replace(']','')
    return lines
    # close the file after reading the lines.
    f.close()



#
highscoreL = Label(gui, text="HIGHSCORE LIJST:", font="Arial 12 bold").place(x=740, y=200)
highscorePositie = Label(gui, text="Positie: ", font="Arial 12 italic").place(x=700, y=250)
highscoreNaam = Label(gui, text="Naam: \n" + str(leesNaam()), font="Arial 12 italic").place(x=800, y=250)
highscoreScore = Label(gui, text="Score: \n" + str(punten), font="Arial 12 italic").place(x=900, y=250)



#MAAK DE HINTKNOP
hintbutton = Button(gui, text="HINT").place(x=900, y=700)

gui.mainloop()
