from tkinter import *

def pakNaam():
    username_entry = naaminput.get()
    stringvoorlabel = "Uw naam is " + username_entry
    labelusername = Label(gui,text=stringvoorlabel, font="Arial 12 bold")
    labelusername.place(x=40, y=700)
    return username_entry

gui = Tk()
gui.title("ReverseAkinator")
gui.geometry("1000x750")

punten = 25

scoredict = {}

#GEEF JE NAAM
naaminput = Entry(gui, text="Voer je username in ")
naaminput.place(x=500, y=500)
naambutton = Button(gui, text="Voer in", command=pakNaam).place(x=600, y=500)

#MAAK DE WIDGETS
score = Label(gui, text=punten, font="Arial 12").place(x=0, y=0)
username = Label(gui, text="USERNAME", font="Arial 12 italic").place(x=0, y=40)
hints = Label(gui, text="HINTLIJST:", font="Arial 12 bold").place(x=450, y=0)
inhoudHintlijst = Label(gui, text="Inhoud", font="Arial 12 italic").place(x=450, y=50)


#MAAK DE HINTKNOP
hintbutton = Button(gui, text="HINT").place(x=900, y=700)

gui.mainloop()
