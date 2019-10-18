import json

import subprocess
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from smartcard.CardType import CardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
from subprocess import Popen, PIPE


class DCCardType(CardType):
    def matches( self, atr, reader=None ):
        return atr[0]==0x3B


def rundd():
    cardtype = DCCardType()
    cardrequest = CardRequest(timeout=1, cardType=cardtype)
    cardservice = cardrequest.waitforcard()
    cardservice.connection.connect()
    output = toHexString(cardservice.connection.getATR())
    # print(output)
    cardservice.connection.getReader()
    new = 'new.txt'
    file = open(new, 'a+')
    file.writelines(output + "\n")
    if output == "3B 9A 94 00 92 02 75 93 11 00 01 02 02 21":
        p = Popen("newWiFiProfile.bat", cwd=r"c:\Users\Babatunde\Desktop\MOES",stdout=PIPE,
                  stderr=subprocess.STDOUT)
        while True:
            out = p.stdout.readline()
            if out == '' and p.poll() is not None:
                break
            T.insert(tk.END, out)
    else:
        print('MOES ID NOT DETECTED (CONNECTION UNSUCCESSFUL)')


root = tk.Tk()
root.title('MOES CONNECTION APP')
label1 = Label(root, text ="CLICK TO CONNECT")
label1.pack(side='top',fill='x')
button = Button(root, text ="Connect", command=rundd)
button.config(fg = 'blue',bg="black")
button.pack(side="top",fill="x")
S = Scrollbar(root)
T = Text(root, height=4, width=500)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=BOTH)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
root.mainloop()