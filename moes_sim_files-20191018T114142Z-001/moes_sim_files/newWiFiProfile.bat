netsh wlan add profile filename = "YinkWiFi.xml"
netsh wlan set profileparameter name=MOES2 SSIDname=MOES2 keymaterial=qwerty123
netsh wlan connect name=MOES2 ssid=MOES2 > report.txt

netsh wlan show networks mode=bssid > signalStrength.txt