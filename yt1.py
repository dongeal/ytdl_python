
from pytube import YouTube



link = input ('youtube link :')
video_object = YouTube(link)

for i in video_object.streams:
    print (str(i.itag)+' '+i.mime_type+' '+i.type)