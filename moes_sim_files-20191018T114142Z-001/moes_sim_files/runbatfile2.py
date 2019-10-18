from smartcard.CardType import CardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
from subprocess import Popen


class DCCardType(CardType):
    def matches( self, atr, reader=None ):
        return atr[0]==0x3B

def call_card():
	cardtype = DCCardType()
	cardrequest = CardRequest( timeout=1, cardType=cardtype )
	cardservice = cardrequest.waitforcard()
	cardservice.connection.connect()
	output = toHexString( cardservice.connection.getATR() )
	print(output)
	print (cardservice.connection.getReader())
	new = 'new.txt'
	file = open(new,'a+')
	file.writelines(output + "\n")
	if output == "3B 9A 94 00 92 02 75 93 11 00 01 02 02 21":
		p = Popen("network1.bat", cwd=r"c:\Users\Babatunde\Desktop")
		stdout, stderr = p.communicate()
		print('the code launched successfully')
if call_card():
	print("connected")
else:
	print("not connnected")        