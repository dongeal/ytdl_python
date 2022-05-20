from pytube import YouTube

def on_complete(stream, filepath):
	print('download complet')
	print(filepath)

def on_progress(stream, chunk, bytes_remaining):
	progress_string = f'{round(100-(bytes_remaining/stream.filesize*100),2)}%'
	print(progress_string)

link= input("youtube link: ")
video_object = YouTube(link, on_complete_callback=on_complete,on_progress_callback= on_progress)

print(f'title: {video_object.title}')
print(f'title: {round(video_object.length/60,2)} minutes')
print(f'title: {video_object.views}')
print(f'title: {video_object.author}')

#download
print('download : (b)est | (w)orst  | (a)udio only | (e)xit')
download_choice = input('choose :')

match download_choice:
	case 'b':
		video_object.streams.get_highest_resolution().download(r"C:\Users\Dongeal\Desktop\youtubeDown")
	case 'w':
		video_object.streams.get_lowest_resolution().download(r"C:\Users\Dongeal\Desktop\youtubeDown")
	case 'a':
		video_object.streams.get_audio_only().download(r"C:\Users\Dongeal\Desktop\youtubeDown")
	