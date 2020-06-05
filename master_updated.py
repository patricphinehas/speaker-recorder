import subprocess
import sys
import os
import gi
import re
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pafy
import webbrowser as wb
from pytube import Playlist
import skip
from pytube import YouTube


class Record:
    def __init__(self):
        self.gladefile = "record_speakers.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("Record_Speakers")
        self.textbox = self.builder.get_object("entry1")
        self.menu = self.builder.get_object("menu1")
        self.infobar = self.builder.get_object("infobar1")
        self.label1 = self.builder.get_object("label1")
        self.label2 = self.builder.get_object("label2")
        self.status_count = 0
        self.window.show()

    def on_Record_Speakers_destroy(self, object, data=None):
        print ("Quit with Cancel")
        Gtk.main_quit()

    def on_switch1_notify(self, switch, gparam):
        music_path = os.environ["HOME"]
        music_path = music_path + "/Music"
        print (music_path)
        if switch.get_active():
            
            self.label1.set_text("Recording Started")

            if len(self.textbox.get_text()) != 0:
                # mp3file = self.textbox.get_text()
                # fileData = pafy.new(mp3file)
                # audio = fileData.audiostreams
                # audio[2].download()

                # get the sub URL's from the playlist
                URL = self.textbox.get_text()
                playlist = Playlist(URL)
                for video_url in playlist.video_urls:
                    print(video_url)
                    video=pafy.new(video_url)
                    print("Video title is :"+video.title)
                    print("Video Duration is :"+video.duration)

                    # skip.skipper()
                    

            else:
                self.label1.set_text("enter url")

        else:
            print ("Stop")
            self.label1.set_text("Recording Stopped")
            subprocess.call(["pkill", "parec"])

if __name__ == "__main__":
  main = Record()
  Gtk.main()
