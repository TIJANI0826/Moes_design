netsh wlan add profile filename = "MOES1.xml"
netsh wlan set profileparameter name=MOES1 SSIDname=MOES1 keymaterial=codel201711
netsh wlan connect name=MOES1 ssid=MOES1