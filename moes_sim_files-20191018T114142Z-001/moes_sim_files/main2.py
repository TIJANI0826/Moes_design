from __future__ import print_function
from time import sleep,time
from subprocess import Popen

from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString
import subprocess
import Tkinter as tk
from Tkinter import *
#from Tkinter.Scrolle import ScrolledText
from smartcard.CardType import CardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
from subprocess import Popen, PIPE


# a simple card observer that prints inserted/removed cards
class PrintObserver(CardObserver):
    """A simple card observer that is notified
    when cards are inserted/removed from the system and
    prints the list of cards
    """

    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            output = toHexString(card.atr)
            T.insert(END, 'sbfnsjbbfbn')
            T.insert(END,"\n")
            T.insert(END ,'+Inserted:  ' + output)

            if output == "3B 9A 94 00 92 02 75 93 11 00 01 02 02 21":
                p = Popen("MOES1.bat", cwd=r"C:\Users\Emmanuel\Desktop\MOES\moes_sim_files",stdout=PIPE,
                  stderr=subprocess.STDOUT)
                d = Popen("MOES2.bat", cwd=r"C:\Users\Emmanuel\Desktop\MOES\moes_sim_files",stdout=PIPE,
                  stderr=subprocess.STDOUT)
                while True:
                    out = p.stdout.readline()
                    if out == '' and p.poll() is not None:
                        T.insert(tk.END, out2)
                        break
                    out2 = d.stdout.readline()
                    if out2 == '' and d.poll() is not None:
                        T.insert(tk.END, out2)
                        break
                    T.insert(tk.END, out2)
                    T.insert(tk.END, out)
                """while True:
                    out = p.stdout.readline()
                    if out == '' and p.poll() is not None:
                        break
                    T.insert(tk.END, out)
                    not_available_1 = 'The network specified by profile "MOES1" is not available to connect.'
                    if out == not_available_1:
                        p2 = Popen("MOES2.bat", cwd=r"c:\Users\Babatunde\Desktop\MOES",stdout=PIPE,
                            stderr=subprocess.STDOUT)
                        while True:
                            out2 = p2.stdout.readline()
                            if out2 == '' and p2.poll() is not None:
                                break
                            T.insert(tk.END, out2)"""
                T.insert(END,'MOES ID MATCHED....')
                T.insert(END,"\n")
                T.insert(END,'CONNECTED TO NETWORK')
            else:
                T.insert(END,"\n")
                T.insert(END,'MOES ID NOT DETECTED (CONNECTION UNSUCCESSFUL)')
        for card in removedcards:
            T.insert(END,"\n")
            T.insert(END,"-Removed: " + toHexString(card.atr))
            p = Popen("disconnect.bat", cwd=r"C:\Users\Emmanuel\Desktop\MOES\moes_sim_files",
                stdout=PIPE, stderr = subprocess.STDOUT)
            T.insert(END,"\n")
            T.insert(END,'MOES CARD REMOVED (WIFI DISCONNECTED)')

if __name__ == '__main__':
    cardmonitor = CardMonitor()
    cardobserver = PrintObserver()

    root = tk.Tk()
    root.title('MOES CONNECTION APP')
    label1 = Label(root, text="CLICK TO CONNECT")
    label1.pack(side='top', fill='x')
    button = Button(root, text="Connect",command=cardmonitor.addObserver(cardobserver))
    button.config(fg='cyan', bg="light green")
    button.pack(side="top", fill="x")
    S = Scrollbar(root)
    T = Text(root, height=4, width=500)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    root.mainloop()

    T.insert(END, "\n")
    T.insert(END, "Insert or remove a smartcard in the system.")
    T.insert(END, "This program will exit in 10 seconds")
    T.insert(END, "")


    sleep(10)

    # don't forget to remove observer, or the
    # monitor will poll forever...

    import sys
    if 'win32' == sys.platform:
        print('press Enter to continue')
        sys.stdin.read(1)
