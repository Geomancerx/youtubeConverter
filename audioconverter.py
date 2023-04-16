from pytube import YouTube
from moviepy.editor import VideoFileClip

# Get the URL of the YouTube video
url = "<link goes here>"

# Download the video using PyTube
yt = YouTube(url)
video = yt.streams.first()
video.download()

# Convert the video to MP3 using MoviePy
clip = VideoFileClip(video.default_filename)
clip.audio.write_audiofile("file/path/here/<desired name>.mp3")

# Print a message to indicate that the conversion is complete
print("Audio conversion complete!")
