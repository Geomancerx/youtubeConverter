# libraries
import yt_dlp

# get the URL of the youtube video
url = "https://www.youtube.com/watch?v=_D0ZQPqeJkk"

# initialize the yt-dlp downloader
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    video_title = info['title']
    ydl.download([url])

# print a message to indicate that the conversion is complete
print(f"Video download complete: {video_title}.mp4")