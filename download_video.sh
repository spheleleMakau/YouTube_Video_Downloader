#!/bin/bash

# Save the URL from the command line
URL=$1

# Run the Docker container with the URL as an argument
docker run -v "$(pwd):/Youtube_video_downloader" -w /Youtube_video_downloader youtube_video_downloader python3 youtube_video_downloader.py "$URL"
