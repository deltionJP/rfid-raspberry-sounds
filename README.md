# Project leerjaar 3
Oorspronkelijk een video player, hier is het iets aangepast zodat ik mp3 bestanden kan afspelen.
Videos werken ook.

Kids love this video player.
This is a great project for folks that are new to programming. 

wat ben je nodig:

* Raspberry Pi 3
* RFID RC522 Kit
* RFID 13.56 MHz Cards

### Follow these instructions on setting up the RFID kit w/ your Pi: 
* [How to setup a Raspberry Pi RFID RC522 Chip - Pi My Life Up](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
* [RFID (RC522) - piddlerintheroot |  piddlerintheroot](https://www.piddlerintheroot.com/rfid-rc522-raspberry-pi/)

### The Raspberry Pi 3 has a video player preinstalled called: OMXPlayer
* [OMXPlayer: An accelerated command line media player - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md)

### Files
* SoundPlay.py - Dit bestand scant de NFC tag en speeld het bestand af (Video is ook mogelijk)
* read.py - Testen van NFC tags.
* write.py - schrijf naam van bestand op NFC tag. Voorbeeld: sound1.mp3


**Code execution at start up**

You can have your code execute at runtime by adding it to the /etc/rc.local file

[rc.local - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)

