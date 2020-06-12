download the whole playlist without hassle

![Speaker Recorder Window](/images/img.png)

Setup for GUI version
-----
1. Run ./install.sh
2. Go to Dash Home, search for speaker recorder
3. copy paste the URL(the playlist)

4. after all downloads complete use the following command if to convert to different audio formats

" audioconvert [--verbose/-v] convert INPUT_DIRECTORY OUTPUT_DIRECTORY [--output-format/-o TARGET_FORMAT] "

TARGET_FORMATS
.mp3
.flac
.aiff
.mp4
.m4a


CLI version
``` python3 cli.py [URL] ```

[p.s. downloads to m4a folder in the application root directory]

[Works on any Debian based distro]
