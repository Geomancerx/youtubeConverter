from pytube import YouTube
from moviepy.editor import VideoFileClip

# Get the URL of the YouTube video
url = "<link goes here>"

# Download the video using PyTube
yt = YouTube(url)
video = yt.streams.first()
video.download()

# Convert the video to MP4 using MoviePy
clip = VideoFileClip(video.default_filename)
clip.write_videofile("file/path/here/<desired name>.mp4")

# Print a message to indicate that the conversion is complete
print("Video conversion complete!")
