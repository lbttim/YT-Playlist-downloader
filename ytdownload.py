import yt_dlp
from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=YOURPLAYLISTID')

for url in p.video_urls:
    print(url)
    video_url = url
    video_info = yt_dlp.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
