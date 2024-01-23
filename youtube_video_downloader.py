from pytube import YouTube
from sys import argv
#this is to be able to run this program name, and the link to the video that we want to download
# Acess the link from the commandLIne in a python code use argv

link = argv[1]

#youtube object for this link
yt = YouTube(link)

#print some info about this vedio we want to download 
print("Title:", yt.title)
print("Views:", yt.views)


#Download the video
y_download = yt.streams.get_highest_resolution()

y_download.download("/home")