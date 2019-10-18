netsh wlan add profile filename = "YinkWiFi.xml"
netsh wlan set profileparameter name=Logeak-Wifi SSIDname=Logeak-Wifi keymaterial=qwerty123
netsh wlan connect name=Logeak-Wifi ssid=Logeak-Wifi > report.txt

netsh wlan show networks mode=bssid > signalStrength.txt