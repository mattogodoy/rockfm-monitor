# RockFM Song Monitor

I have a theory that I want to prove: RockFM Madrid (101.7 FM) plays the same songs over and over, specially Bon Jovi, which they seem to be in love with.

This is a simple Python program that connects to the same API used by the oficial online radio, gets the song being played and stores it in a CSV file for later analysis.

- The results are stored in a file called **history.csv**
- The CSV format of the history file is [son author, song title, date(dd/mm/yyyy), time(hh:mm)]
- New songs are checked every 20 seconds (just as in the official online radio page)
- Songs are not saved twice if a check happens while the same song is still being played

## Used modules

These modules are required in order for this program to run:

- requests
- time
- schedule
- json
- os

## Execution

This program is meant to run under **python3**.

### Monitor

The monitor script runs in the background and captures the songs being played.

`python3 monitor.py`

The songs will be checked every **20** seconds (only if the program is running).


### Results

The results script reads the contents of the history file and shows some statistics.

`python3 results.py`

The output will show something like this:

![Results output](img/rockfm.png?raw=true "Results output")
