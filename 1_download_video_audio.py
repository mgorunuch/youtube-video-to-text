import yt_dlp as youtube_dl
from config import Config
import os

VIDEO_URL = Config.video_url


def download_ytvid_as_mp3():
    filename = f"output.mp4"
    options = {
        'format':    'bestaudio[ext=mp4]',
        'keepvideo': False,
        'outtmpl':   os.path.join(os.getcwd(), 'tmp', filename),
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([Config.video_url])
    print("Download complete... {}".format(filename))


if __name__ == "__main__":
    download_ytvid_as_mp3()
