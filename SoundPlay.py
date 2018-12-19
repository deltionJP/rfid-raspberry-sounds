#!/usr/bin/env python
from random import randint
import SimpleMFRC522
import time
import subprocess
import os
import logging
import random
import glob
import RPi.GPIO as GPIO


def playsound(video, loop = 0):

	global myprocess
	global directory

	logging.debug('linux: omxplayer %s' % video)

	proccount = isplaying()

	if proccount == 1 or proccount == 0:

		logging.debug('No videos playing, so play video')

	else:

		logging.debug('Video already playing, so quit current video, then play')
		myprocess.communicate(b"q")
		
	if loop == 0:
		myprocess = subprocess.Popen(['omxplayer',directory + video],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
	
	else:
		myprocess = subprocess.Popen(['omxplayer','--loop',directory + video],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
	
	time.sleep(3)

def isplaying():

		"""check if omxplayer is running
		if the value returned is a 1 or 0, omxplayer is NOT playing a video
		if the value returned is a 2, omxplayer is playing a video"""

		processname = 'omxplayer'
		tmp = os.popen("ps -Af").read()
		proccount = tmp.count(processname)

		return proccount


#program start

logging.basicConfig(level=logging.DEBUG)

reader = SimpleMFRC522.SimpleMFRC522()

directory = '/home/pi/sounds/'

print("Begin Player")

try:
	while True: 

		proccount = isplaying()

		if proccount == 1 or proccount == 0:

			current_sound_id = long(10)
			

		
		start_time = time.time()

		logging.debug("Waiting for ID to be scanned")
		id, sound_name = reader.read()

		logging.debug("ID: %s" % id)
		logging.debug("Sound Name: %s" % sound_name)

		sound_name = sound_name.rstrip()

		if current_sound_id != id:

			logging.debug('New sound')
			#this is a check in place to prevent omxplayer from restarting video if ID is left over the reader.
			#better to use id than sound_name as there can be a problem reading sound_name occasionally
			

			if sound_name.endswith(('.mp3')):
				current_sound_id = id 	#we set this here instead of above bc it may mess up on first read
				logging.debug("playing: omxplayer %s" % sound_name)
				playsound(sound_name)

		else:

			end_time = time.time()
			elapsed_time = end_time - start_time
			proccount = isplaying()

			if proccount != 1 and proccount != 0:

				if elapsed_time > 0.6:
					#pause, unpause sound

					logging.debug('Pausing sound - or - Playing sound')
					myprocess.stdin.write("p")


except KeyboardInterrupt:
	GPIO.cleanup()
	print("\nAll Done")
