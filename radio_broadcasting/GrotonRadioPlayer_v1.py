import glob, os
import vlc
import time
import random
from datetime import datetime
from openpyxl import Workbook, load_workbook
from datetime import date, datetime

class GrotonRadioPlayer:
	def __init__(self):
		self.songsInCurrentDirectory = []
		self.listOfDirectories = []

		self.recently_played = []
		self.currently_playing = None
		self.requestList = []
		self.stationPlayer = None
		self.mediaInfo = []
		self._date = datetime.today()
		self.currentHour = self._date.hour

		#program will officially stop running at 3pm
		self.requestHour = 9
		self.closingTime = 3

	def collectSongFiles(self):
		filestem = '/home/sdl5384/Desktop/'
		for file in os.listdir('/home/sdl5384/Desktop'):
			if file.endswith('.mp3'):
				self.songsInCurrentDirectory.append(filestem+file)
		print(self.songsInCurrentDirectory)

	def searchForSong(self,songName):
		songFilePath = ''
		return songFilePath

	def countSubFolders(self,filepath):
		count = 0
		for j  in range(0,len(filepath)-1):
			if filepath[j] == '/':
				count = count + 1

		return count

	def pickNextSong(self):
		#pick next song either randomly or by request
		if self.currentHour == self.requestHour:
			#pick the next song from the request list
			i = 0
			while (i <= len(self.requestList)):
				#find song in directory
				filepath = self.searchForSong(self.requestList[i])
		#randomly choose song if not request hour
		else:
			filepath = random.choice(self.songsInCurrentDirectory)
		return filepath

	def playSong(self,mp3Filepath):
		self.stationPlayer = vlc.MediaPlayer(mp3Filepath)
		self.stationPlayer.play()
		#test if song is still playing
		time.sleep(1)

		while (self.stationPlayer.is_playing()):
			time.sleep(1)

	def extractInfo(self,filepath):
		#return a list of information of mp3 in question
		trackMetadata = []
		# artist/band first, song name second, and then time the song stopped playing
		return None

	def updateRecentlyPlayed(self,filepath):
		if self.stationPlayer == 0:
			self.extractSongInfo(filepath)
			self.recently_played.append(self.mediaInfo)

	def updateRequestList(self):
		return None

def main(self):
	G = GrotonRadioPlayer()
	while (self.currentHour != self.closingTime):
		G.collectSongFiles()
		track = G.pickNextSong()
		components = track.split('/')
		song = track[len(track)-1]
		self.currently_playing = song
		songPlaying = "Currently playing " + self.currently_playing

		keepMusicPlaying = True
		while keepMusicPlaying:
			G.playSong(track)

			time.sleep(3)
			track = G.pickNextSong()

		#update currentHour variable to keep checking on time
		#program will expire once self.currentHour matches the value of self.closingTime

G = GrotonRadioPlayer()
main(G)