import pytube
from pytube import YouTube

link = input("type a youtube url: ")
yt = YouTube(link)
print(yt.title)
video_download = pytube.YouTube(link)
video_download.streams.get_highest_resolution().download()
print('Video Downloaded', link)