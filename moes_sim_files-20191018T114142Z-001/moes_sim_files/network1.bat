netsh wlan add profile filename = "network1.xml"
netsh wlan set profileparameter name=MOES1 SSIDname=MOES1 keymaterial=codel201711
netsh wlan connect name=MOES1 ssid=MOES1 > report.txt

netsh wlan show networks mode=bssid > signalStrength.txt