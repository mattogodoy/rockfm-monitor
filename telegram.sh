#!/bin/bash

# In order for this to work, you have to install 'telegram-send' and 'imagemagick':
#   pip3 install telegram-send
#   brew install imagemagick (Mac)
#   sudo apt-get install imagemagick (Linux)

# Generate the results and save them to an image
#python3 results.py | convert -font consolas -pointsize 40 label:@- stats.png # For Mac
python3 results.py | convert -font /usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf -pointsize 40 label:"`tee`" stats.png # For Linux

# Send the created image as a file via Telegram
telegram-send --image stats.png --caption "The latest RockFM statistics"