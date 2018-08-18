import requests
import time
import schedule
import json
import os

os.environ['TZ'] = 'Europe/Madrid' # To fix server's different time zone configuration

lastSong = None


# Main program
def main():
  getLastSong() # Get the last song from the history file
  getCurrentSong() # Run for the first time before scheduling

  schedule.every(20).seconds.do(getCurrentSong) # Configure the schedule

  # Run an infinite loop that checks the schedule
  while 1:
    schedule.run_pending()
    time.sleep(1)


class Song:
  # Constructor
  def __init__(self, author, title):
    self.author = author.lower().replace(',', '') # Remove commas because of CSV
    self.title = title.lower().replace(',', '') # Remove commas because of CSV

    if(self.title == 'rockfm'):
      self.author = 'rockfm'
      self.title = 'intermission'

  # Allows to compare different instances of the
  # same class by it's attributes
  def __eq__(self, other):
    return self.__dict__ == other.__dict__

  def save(self):
    currentDate = time.strftime("%d/%m/%Y")
    currentTime = time.strftime("%H:%M")
    line = self.author + ',' + self.title + ',' + currentDate + ',' + currentTime + '\n'

    with open("history.csv", "a") as historyFile:
      historyFile.write(line)

    print("Song added to history file.")


# Gets te current playing song
def getCurrentSong():
  global lastSong # Obtain access to global variable. No static variables in python 🤷🏻‍

  apiUrl = 'http://bo.cope.webtv.flumotion.com/api/active?format=json&podId=78'

  # Sometimes the API calls fail, so let's make it crash-proof
  try:
    req = requests.get(apiUrl) # Make API call
    data = req.json() # Convert results to a JSON object
    data = json.loads(data['value']) # The valuable data comes inside 'value', and also in JSON format

    currentSong = Song(data['author'], data['title'])

    if(currentSong != lastSong):
      print("New song playing: ", currentSong.author, ' - ', currentSong.title)
      currentSong.save()
      lastSong = currentSong

  except:
    print("API call failed. Retrying in a few seconds... ")


# Gets the last song in the history file
def getLastSong():
  global lastSong

  with open('history.csv', 'r') as historyFile:
    lines = historyFile.read().splitlines()
    lastLine = lines[-1] # Get the last line in the file
    author = lastLine.split(',')[0]
    title = lastLine.split(',')[1]
    lastSong = Song(author, title)


# Run the main program
main()
