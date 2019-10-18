from __future__ import print_function
from time import sleep,time
from subprocess import Popen

from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString
import subprocess
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from smartcard.CardType import CardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
from subprocess import Popen, PIPE


# a simple card observer that prints inserted/removed cards
class RunIt():
    def update(self,CardObserver,observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            output = toHexString(card.atr)
            self.T.insert(END,"\n")
            self.T.insert(END ,'+Inserted:  ' + output)
            if output == "3B 9A 94 00 92 02 75 93 11 00 01 02 02 21":
                p = Popen("MOES1.bat", cwd=r"c:\Users\Babatunde\Desktop\MOES",stdout=PIPE,
                    stderr=subprocess.STDOUT)
                while True:
                    out = p.stdout.readline()
                    d = p.stdout.readline()
                    if out == '' and p.poll() is not None:
                        break
                    self.T.insert(tk.END, out)
                self.T.insert(END,'MOES ID MATCHED....')
                self.T.insert(END,"\n")
                self.T.insert(END,'CONNECTED TO NETWORK')
            else:
                self.T.insert(END,"\n")
                self.T.insert(END,'MOES ID NOT DETECTED (CONNECTION UNSUCCESSFUL)')
            for card in removedcards:
                self.T.insert(END,"\n")
                self.T.insert(END,"-Removed: " + toHexString(card.atr))
                p = Popen("disconnect.bat", cwd=r"C:\Users\Babatunde\Desktop\MOES",
                    stdout=PIPE, stderr = subprocess.STDOUT)
                self.T.insert(END,"\n")
                self.T.insert(END,'MOES CARD REMOVED (WIFI DISCONNECTED)')


    root = tk.Tk()
    root.title('MOES CONNECTION APP')
    label1 = Label(root, text="CLICK TO CONNECT")
    label1.pack(side='top', fill='x')
    button = Button(root, text="Connect",command=update)
    button.config(fg='cyan', bg="light green")
    button.pack(side="top", fill="x")
    S = Scrollbar(root)
    T = Text(root, height=4, width=500)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
"""
    T.insert(END, "\n")
    T.insert(END, "Insert or remove a smartcard in the system.")
    T.insert(END, "This program will exit in 10 seconds")
    T.insert(END, "")"""


if __name__ == '__main__':
    sleep(10)

    # don't forget to remove observer, or the
    # monitor will poll forever...

    import sys
    if 'win32' == sys.platform:
        print('press Enter to continue')
        sys.stdin.read(1)
