import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget	
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from smartcard.CardType import CardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
from subprocess import Popen

class DCCardType(CardType):
    def matches( self, atr, reader=None ):
        return atr[0]==0x3B



class Lesson1App(App):
    def rundd(self):
        cardtype = DCCardType()
        cardrequest = CardRequest( timeout=1, cardType=cardtype )
        cardservice = cardrequest.waitforcard()
        cardservice.connection.connect()
        output = toHexString( cardservice.connection.getATR() )
        #print(output)
        cardservice.connection.getReader()
        new = 'new.txt'
        file = open(new,'a+')
        file.writelines(output + "\n")
        if output == "3B 9A 94 00 92 02 75 93 11 00 01 02 02 21":
            p = Popen("newWiFiProfile.bat", cwd=r"c:\Users\Babatunde\Desktop\MOES")
            stdout, stderr = p.communicate()
            print('the code launched successfully')
        else:
            print('MOES ID NOT DETECTED (CONNECTION UNSUCCESSFUL)')

     
    def build(self):
        lbl=Button(command =self.rundd )
        #lbl is a variable name being assigned the Label definition
        return lbl #This  must match the name of the Widget you want to appear on screen

if __name__ == '__main__': #Documentation suggests that each program file should be called main.py but I think that only matters if you're creating the final App to go onto a phone or tablet we're a long way off from that yet

    Lesson1App().run() #This must match the name of your App
 