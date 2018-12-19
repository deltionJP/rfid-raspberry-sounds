# Project leerjaar 3
Oorspronkelijk een video player, hier is het iets aangepast zodat ik mp3 bestanden kan afspelen.
Videos werken ook.


wat ben je nodig:

* Raspberry Pi 3
* RFID RC522 Kit
* RFID 13.56 MHz Cards

### Hieronder staan sites met informatie hoe je je RaspberryPi gebruikt met RC522 NFC reader: 
* [How to setup a Raspberry Pi RFID RC522 Chip - Pi My Life Up](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
* [RFID (RC522) - piddlerintheroot |  piddlerintheroot](https://www.piddlerintheroot.com/rfid-rc522-raspberry-pi/)

De lijn hieronder geeft aan waar de muziek/video fragmenten staan, deze kan je uiteraard aanpassen.
```
# SoundPlay.py
directory = '/home/pi/sounds/'
```
### De Raspberry Pi 3 heeft een video/muziek player ingebouwd die werkt via de terminal : OMXPlayer
* [OMXPlayer: An accelerated command line media player - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md)

### Bestanden
* SoundPlay.py - Dit bestand scant de NFC tag en speeld het bestand af (Video is ook mogelijk)
* read.py - Testen van NFC tags.
* write.py - schrijf naam van bestand op NFC tag. Voorbeeld: sound1.mp3


**Code automatisch uitvoeren**

Met het bestand /etc/rc.local kan je, doormiddel van toevoegen van:
```
# /ect/rc.local
python /home/pi/projectmap/SoundPlay.py
```
Automatisch laten afspelen.

[rc.local - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)

