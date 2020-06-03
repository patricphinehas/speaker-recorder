# from pytube import Playlist
# playlist = Playlist('https://www.youtube.com/watch?v=9smIgRhWpHU&list=PL2WDrOkJHGRsEWWDiHfQujGm8XwTQGryu')
# count =0
# print('Number of videos in playlist: %s' % len(playlist.video_urls))
# for video_url in playlist.video_urls:
#     count+=1
#     print(video_url)
# print(count)



from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=QL82ZcCcM4E')

yt.length
