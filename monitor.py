import requests
import time
import schedule
from os import path


# Main program
def main():
  mergeSongs() # Run for the first time before scheduling
  schedule.every(20).minutes.do(mergeSongs) # Configure the schedule

  # Run an infinite loop while checking the schedule
  while 1:
    schedule.run_pending()
    time.sleep(1)


# Add the last non-repeated songs to the history
def mergeSongs():
  global newHistory

  newHistory = []
  oldHistory = getOldHistory() # Get old history songs

  print("Checking for the last songs...")

  for song in getLastSongs():
    fullName = song['streamTitle'].lower()
    newHistory.append(fullName)

    if fullName not in oldHistory:
      saveNewSong(fullName)

  oldHistory = newHistory
  saveOldHistory(oldHistory)
  print("Current time: " + time.strftime("%H:%M:%S") + " - Waiting 20 minutes until the next check...")


# Gets the last 10 songs from the radio.es API
def getLastSongs():
  # api-endpoint
  APIurl = 'https://api.radio.es/info/v2/search/nowplaying'

  # defining a params dict for the parameters to be sent to the API
  APIparams = {
    '_': '1531576923971',
    'apikey': 'df5cadfe49eeaff53727bad8c69b47bdf4519123',
    'numberoftitles': '10',
    'station': '14160'
  }

  # sending get request and saving the response as response object
  r = requests.get(url = APIurl, params = APIparams)

  # extracting data in json format
  data = r.json()
  data = data[::-1] # Reverse the array so the songs are in descending order
  return data

# Gets the contents of the old hisory as a list
def getOldHistory():
  if path.isfile('old_history.txt'):
    with open('old_history.txt') as file:
      lines = [line.rstrip('\n') for line in file]

    return lines
  else:
    return []


# Saves the oldHistory list to a file
def saveOldHistory(songList):
  oldHistoryFile = open('old_history.txt', 'w')

  for song in songList:
    oldHistoryFile.write(song + '\n')


# Appends a new song to the end of the history file
def saveNewSong(song):
  print("New song found: " + song)

  artistName = song.split(' - ')[0]
  songName = song.split(' - ')[1]
  currentDate = time.strftime("%d/%m/%Y")
  currentTime = time.strftime("%H:%M:%S")
  line = artistName + ', ' + songName + ', ' + currentDate + ', ' + currentTime + '\n'

  with open("history.csv", "a") as historyFile:
    historyFile.write(line)


# Run the main program
main()
