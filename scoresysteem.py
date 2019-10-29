
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

# while True:
#     x = input(' a is goed, b is fout, c is hint: ')
#     if x == 'a':
#         print(goed())
#     elif x == 'b':
#         print(fout())
#     elif x == 'c':
#         print(hint())
