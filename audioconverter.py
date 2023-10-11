# imported libraries
import yt_dlp
from pydub import AudioSegment

# get the URL of the youtube video
url = "youtube-url-here"

# initialize the yt-dlp downloader
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    video_title = info['title']
    ydl.download([url])

# convert the video to mp3 using pydub
video_path = f'{video_title}.mp3'
mp3_path = '/file/path/here/<filename>.mp3'

audio = AudioSegment.from_mp3(video_path)
audio.export(mp3_path, format="mp3")

# print a message to indicate that the conversion is complete
print("Audio conversion to MP3 complete!")