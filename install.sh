#!/bin/bash

sudo echo "Getting Stuffs ready, sit back and have ☕"
sudo apt-get install pulseaudio-utils lame scrot python3-tk python3-dev pyautogui python3-opencv -y

DIR=/usr/local/bin/record-speakers
if [ ! -d "$DIR" ]; then
	sudo mkdir $DIR
fi
sudo cp record_speakers.py record-spreakers.svg record_speakers.glade /usr/local/bin/record-speakers
cp record_speakers.desktop ${HOME}/.local/share/applications/
