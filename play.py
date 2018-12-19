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


def playmovie(video, loop = 0):

	"""plays a video."""

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

def playmenu():

		logging.debug('No videos playing, play menu')

		selectmenu = randint(1,2)
		if selectmenu == 1: menuvid = "song1.mp3"
		elif selectmenu == 2: menuvid = "song1.mp3"

		playmovie(menuvid,1)

#program start

logging.basicConfig(level=logging.DEBUG)

reader = SimpleMFRC522.SimpleMFRC522()

directory = '/media/pi/songs/'

print("Begin Player")

try:
	while True: 

		proccount = isplaying()

		if proccount == 1 or proccount == 0:

			current_movie_id = long(10)
			
			playmenu()

		
		start_time = time.time()

		logging.debug("Waiting for ID to be scanned")
		id, movie_name = reader.read()

		logging.debug("ID: %s" % id)
		logging.debug("Movie Name: %s" % movie_name)

		movie_name = movie_name.rstrip()

		if current_movie_id != id:

			logging.debug('New Movie')
			#this is a check in place to prevent omxplayer from restarting video if ID is left over the reader.
			#better to use id than movie_name as there can be a problem reading movie_name occasionally
			

			if movie_name.endswith(('.mp3', '.avi', '.m4v','.mkv')):
				current_movie_id = id 	#we set this here instead of above bc it may mess up on first read
				logging.debug("playing: omxplayer %s" % movie_name)
				playmovie(movie_name)

			elif 'folder' in movie_name:
				current_movie_id = id
				movie_directory = movie_name.replace('folder',"") 
				movie_name = random.choice(glob.glob(os.path.join(directory + movie_directory, '*')))
				movie_name = movie_name.replace(directory,"")

				logging.debug("randomly playing: omxplayer %s" % movie_name)
				playmovie(movie_name)

		else:

			end_time = time.time()
			elapsed_time = end_time - start_time
			proccount = isplaying()

			if proccount != 1 and proccount != 0:

				if elapsed_time > 0.6:
					#pause, unpause movie

					logging.debug('Pausing movie - or - Playing movie')
					myprocess.stdin.write("p")


except KeyboardInterrupt:
	GPIO.cleanup()
	print("\nAll Done")

