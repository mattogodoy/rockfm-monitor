# RockFM Song Monitor

I have a theory that I want to prove: RockFM Madrid (101.7 FM) plays the same songs over and over, specially Bon Jovi, which they seem to be in love with.

This is a simple Python program that connects to the same API used by the oficial online radio, gets the song being played and stores it in a CSV file for later analysis.

- The results are stored in a file called **history.csv**
- The CSV format of the history file is [artist, song name, date(dd/mm/yyyy), time(hh:mm:ss)]
- New songs are checked every 20 seconds (just as in the official online radio page)

## Used modules

These modules are required in order for this program to run:

- requests
- time
- schedule
- json
- os

## Execution

This program is meant to run under **python3**, and you can do so by:

`python3 monitor.py`

The songs will be checked every **20** seconds (only if the program is running).

## To-Do

In a near future I'll code a program to get statistics about the artists, songs and their frequency of broadcast.
