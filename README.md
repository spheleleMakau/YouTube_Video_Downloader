# YouTube_Video_Downloader
YouTube Video Downloader is a Python script that allows users to download YouTube videos effortlessly. The script utilizes the pytube library to interact with YouTube and fetch video details.


### Features:
## Dockerized Solution:

The project is containerized using Docker to eliminate the need for users to install dependencies manually.

## Simple Shell Script:

Users can download YouTube videos by running a provided shell script with the video link as an argument.


## Prerequisites:
Linux/ Mac OS

Docker

## Installation:
Clone this repository:

  ```bash
    
    git clone https://github.com/spheleleMakau/YouTube_Video_Downloader.git
```



Navigate to the project directory:

```bash
    
  
cd  Youtube_video_downloader
```

## build your image


   ```bash
    sudo docker build -t youtube_video_downloader .
```



## To download a youtube video run:

   ```bash
    
 ./download_video.sh <put your URL youtube link here>
```

## See The Magic on "downloaded" folder of this directory
The downloaded videos will be available in the 'downloaded' folder within the project directory.
# Enjoy your videos offline !!!!!!!!!!!

## Contributing
Contributions are welcome! If you have any improvements or suggestions, feel free to create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


 

