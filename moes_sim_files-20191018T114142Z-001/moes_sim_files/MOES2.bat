netsh wlan add profile filename = "MOES2.xml"
netsh wlan set profileparameter name=MOES2 SSIDname=MOES2 keymaterial=qwerty123
netsh wlan connect name=MOES2 ssid=MOES2