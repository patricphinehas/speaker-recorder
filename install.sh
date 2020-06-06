#!/bin/bash

sudo echo "Getting Stuffs ready, sit back and have ☕"
sudo apt-get install pulseaudio-utils lame scrot python3-tk python3-dev pyautogui -y
echo "pip3 install -r requirements.txt"
DIR=/usr/local/bin/record-speakers
if [ ! -d "$DIR" ]; then
	sudo mkdir $DIR
fi
sudo cp master.py record-spreakers.svg record_speakers.glade /usr/local/bin/record-speakers
# sudo cp /images/*.* /usr/local/bin/record-speakers/images
cp record_speakers.desktop ${HOME}/.local/share/applications/
