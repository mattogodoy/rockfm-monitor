# RockFM Song Monitor

I have a therory that I want to prove: RockFM Madrid (101.7 FM) plays the same songs over and over, specially Bon Jovi, which they seem to be in love with.

This is a simple Python program that connects to the **radio.es** API, gets the latest played songs and stores them in a CSV file for later analysis.

## Variables

All of the parameters are currently hardcoded, but these are the most important:

- The results are stored in a file called **history.csv**
- The results of the 10 last songs played by the radio are stored in a file called **old_history.txt**. This allows the program to be closed and restarted without adding repeated songs to the history file.
- The CSV format of the history file is [artist, song name, date(dd/mm/yyyy), time(hh:mm:ss)]
- New songs are checked every 20 minutes

## Used modules

These modules are required in order for this program to run:

- requests
- time
- schedule
- os

## Execution

This program is meant to run under **python3**, and you can do so by:

`python3 monitor.py`

The songs will be checked every **20** minutes (only if the program is running).

## To-Do

I plan to gather enough information to confirm my suspicions, so in a near future I'll code a program to get statistics about the artists, songs and their frequency of broadcast.
