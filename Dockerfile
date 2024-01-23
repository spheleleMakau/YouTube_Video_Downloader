# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /Youtube_video_downloader

# Copy the necessary files into the container
COPY youtube_video_downloader.py .
COPY requirements.txt .

# Create and activate a virtual environment
RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the script
CMD ["venv/bin/python", "youtube_video_downloader.py"]
