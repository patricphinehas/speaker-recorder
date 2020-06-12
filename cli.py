import sys
import pafy
from pytube import Playlist,YouTube

URL = sys.argv[1]
print(URL)
playlist = Playlist(URL)
print(playlist)
for video_url in playlist.video_urls:
# print(video_url)
    try:
        video=pafy.new(video_url)
        bestaudio = video.getbestaudio(preftype = "m4a", ftypestrict = "True")
        print("Video title is :"+video.title)
        # print("Video Duration is :"+video.duration)
        # print("audio quality :" + bestaudio.bitrate)
        bestaudio.download(filepath="m4a")
        # print("download")
    except:
        continue