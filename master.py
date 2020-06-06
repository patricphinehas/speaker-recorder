import subprocess
import sys
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pafy
from pytube import Playlist
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
                # get the sub URL's from the playlist
                # https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj
                URL = self.textbox.get_text()
                playlist = Playlist(URL)
                for video_url in playlist.video_urls:
                    print(video_url)
                    video=pafy.new(video_url)
                    bestaudio = video.getbestaudio(preftype = "m4a", ftypestrict = "True")
                    print("Video title is :"+video.title)
                    print("Video Duration is :"+video.duration)
                    print("audio quality :" + bestaudio.bitrate)
                    bestaudio.download(filepath="m4a")
                    print("download")
                # still under tests for audio conversions for further processing
                # os.system('audioconvert -v /m4a /mp3 -o mp3')
                    
            else:
                self.label1.set_text("enter url")

        else:
            print ("Stop")
            self.label1.set_text("Recording Stopped")
            subprocess.call(["pkill", "parec"])

if __name__ == "__main__":
  main = Record()
  Gtk.main()
