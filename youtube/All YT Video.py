from pytube import YouTube
from time import sleep

url_grab = input("Give me the URL of a video! ")

yt = YouTube(url_grab)

title = yt.title

stream = yt.streams.first()

print("Downloading", '"' + title + '"')
sleep(3)
stream.download('videos')
sleep(0.8)
print("Finished!")