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


class PrintObserver(CardObserver):
    """A simple card observer that is notified
    when cards are inserted/removed from the system and
    prints the list of cards
    """

    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            output = toHexString(card.atr)
            print("\n")
            print('+Inserted:  ' + output)
            if output == "3B 9A 94 00 92 02 75 93 11 00 01 02 02 21":
                p = Popen("MOES1.bat", cwd=r"C:\Users\D_prince Abdulhamid\Desktop\WRITING\moes_sim_files",stdout=PIPE,
                  stderr=subprocess.STDOUT)
                d = Popen("MOES2.bat", cwd=r"C:\Users\D_prince Abdulhamid\Desktop\WRITING\moes_sim_files",stdout=PIPE,
                  stderr=subprocess.STDOUT)
                while True:
                    out = p.stdout.readline()
                    if out == '' and p.poll() is not None:
                        print(out2)
                        break
                    out2 = d.stdout.readline()
                    if out2 == '' and d.poll() is not None:
                        print(out2)
                        break
                    print(out2)
                    print(out)
                
                print('MOES ID MATCHED....')
                print("\n")
                print('CONNECTED TO NETWORK')
            else:
				print("\n")
				print('MOES ID NOT DETECTED (CONNECTION UNSUCCESSFUL)')
        for card in removedcards:
			print("\n")
			print("-Removed: " + toHexString(card.atr))
			p = Popen("disconnect.bat", cwd=r"C:\Users\Emmanuel\Desktop\MOES\moes_sim_files",
                stdout=PIPE, stderr = subprocess.STDOUT)
			print("\n")
			print('MOES CARD REMOVED (WIFI DISCONNECTED)')
if __name__ == '__main__':
	cardmonitor = CardMonitor()
	cardobserver = PrintObserver()
	cardmonitor.addObserver(cardobserver)
