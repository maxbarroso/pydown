from pytube import YouTube
link = input('Link: ')
yt = YouTube(link)
yd = yt.streams.get_highest_resolution()
yd.download()

