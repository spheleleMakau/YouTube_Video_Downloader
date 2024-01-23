from pytube import YouTube
from sys import argv
import os

# Access the link from the command line in a Python code using argv
link = argv[1]

# YouTube object for this link
yt = YouTube(link)

# Print some info about this video we want to download
print("Title:", yt.title)
print("Views:", yt.views)

# Create a 'downloaded' folder if it doesn't exist
download_folder = "downloaded"
os.makedirs(download_folder, exist_ok=True)

# Download the video to the 'downloaded' folder
download_path = os.path.join(download_folder, yt.title + ".mp4")
y_download = yt.streams.get_highest_resolution()
y_download.download(download_folder)

print(f"Video downloaded and saved at: {download_path}")
