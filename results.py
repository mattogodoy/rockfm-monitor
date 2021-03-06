from datetime import date
from collections import Counter


def main():
  history = getHistory()
  songs = []
  artists = []

  startDate = history[0].split(',')[2]
  endDate = history[-1].split(',')[2]

  sDate = date(int(startDate[6:]), int(startDate[3:5]), int(startDate[0:2]))
  eDate = date(int(endDate[6:]), int(endDate[3:5]), int(endDate[0:2]))

  period = (eDate - sDate).days

  print('\n')
  print('  Data collected from {0} to {1} ({2} days)'.format(startDate, endDate, period))
  print('  {0} total songs'.format(len(history)))
  print('\n')

  # Create list of songs
  for song in history:
    songs.append(song.split(',')[0] + ' - ' + song.split(',')[1])

  # Create list of artists
  for artist in history:
    artists.append(artist.split(',')[0])

  songsCount = Counter(songs) # Counts the repeated items in the list
  songsCount = sorted(songsCount.items(), key=lambda kv: kv[1]) # Sort dictionary by values. Returns a list.
  songsCount = songsCount[::-1] # Reverse the list order

  artistsCount = Counter(artists) # Counts the repeated items in the list
  artistsCount = sorted(artistsCount.items(), key=lambda kv: kv[1]) # Sort dictionary by values. Returns a list.
  artistsCount = artistsCount[::-1] # Reverse the list order

  print('{:=^81}'.format(''))
  print('{:=^81}'.format(' TOP 20 SONGS '))
  print('{:=^81}'.format(''))
  print('\n{: ^50} {: ^15} {: ^15}\n'.format('SONG NAME', 'TIMES TOTAL', 'TIMES PER DAY'))

  for song, count in songsCount[:20]:
    print(' {: <50} {: ^15} {: ^15}'.format(song, count, round(count / period, 1)))

  print('\n\n')
  print('{:=^81}'.format(''))
  print('{:=^81}'.format(' TOP 20 ARTISTS '))
  print('{:=^81}'.format(''))
  print('\n{: ^50} {: ^15} {: ^15}\n'.format('ARTIST NAME', 'TIMES TOTAL', 'TIMES PER DAY'))

  for artist, count in artistsCount[:20]:
    print(' {: <50} {: ^15} {: ^15}'.format(artist, count, round(count / period, 1)))

  print('\n')


def getHistory():
  with open('history.csv', encoding='utf-8') as f:
    content = f.readlines()

  content = [x.strip() for x in content] # remove whitespace characters like `\n` at the end of each line
  content = [x for x in content if x.split(',')[0] != 'rockfm'] # Remove RockFM's intermissions
  return content


if __name__ == "__main__":
  main()