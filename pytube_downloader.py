# pytube 이용 다운로드
import tkinter.ttk as ttk
from cProfile import label
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import os
import subprocess
from pytube import YouTube

def on_complete(stream, filepath):
	print('download complet')
	print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress = round(100-(bytes_remaining/stream.filesize*100),2)
    p_var.set(progress)
    progress_bar.update()
    print(progress)

# link= input("youtube link: ")
# video_object = YouTube(link, on_complete_callback=on_complete,on_progress_callback= on_progress)

# print(f'title: {video_object.title}')
# print(f'title: {round(video_object.length/60,2)} minutes')
# print(f'title: {video_object.views}')
# print(f'title: {video_object.author}')

# #download
# print('download : (b)est | (w)orst  | (a)udio only | (e)xit')
# download_choice = input('choose :')

# match download_choice:
# 	case 'b':
# 		video_object.streams.get_highest_resolution().download(r"C:\Users\Dongeal\Desktop\youtubeDown")
# 	case 'w':
# 		video_object.streams.get_lowest_resolution().download(r"C:\Users\Dongeal\Desktop\youtubeDown")
# 	case 'a':
# 		video_object.streams.get_audio_only().download(r"C:\Users\Dongeal\Desktop\youtubeDown")
	
root = Tk()
root.title("Youtube DownLoader--by Dongeal Im")
root.geometry("640x600+300+100")
root.resizable(False,False) 

canvas=Canvas(root)
canvas.pack()
logo_img=PhotoImage(file="youtube.png")
logo_img=logo_img.subsample(2,2)
canvas.create_image(180,100,image=logo_img) 



# 함수 선언---------

# 저장경로

def browse_dest_path():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    if folder_selected =="":
        return
    entry_dest_path.delete(0, END) 
    entry_dest_path.insert(0,folder_selected)
  

def url_download():
    url=url_name.get()
    p_var.set(0)
    video_object = YouTube(url, on_complete_callback=on_complete,on_progress_callback= on_progress)
    
    if len(entry_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장경로를 선택하세요")
        return
    if len(url_name.get()) == 0:
        msgbox.showwarning("경고", "동영상 Url을 입력하세요")
        return    
   
    match flty.get():
        case '1':
           root.title("고화질 동영상 다운로드 중 ---")
           video_object.streams.get_highest_resolution().download(folder_selected)
          
        case '2':
           root.title("저화질 동영상 다운로드 중 ---")
           video_object.streams.get_lowest_resolution().download(folder_selected)
        
        case '3':
            root.title("mp3 다운로드 중 ---")
            video_object.streams.get_audio_only().download(folder_selected)
            file_name=video_object.title
            os.chdir(folder_selected)
            os.rename(file_name+".mp4", file_name+".mp3")
        
        
    root.title("다운로드 완료")
# 동영상 저장로 지정 화면

path_frame=LabelFrame(root, text="저장경로")
path_frame.pack(fill="x")

entry_dest_path=Entry(path_frame)
entry_dest_path.pack(side="left", fill="x", expand=TRUE,padx=10, pady=10, ipady=5)

b_dest_path=Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
b_dest_path.pack(side="right")

# 다운받을 동영상 Url 임력후 다운로드 화면

url_frame = LabelFrame(root, text="동영상 url")
url_frame.pack(fill="x")

url_name =Entry(url_frame)
url_name.pack(side="left", fill="x", expand=TRUE,padx=10, pady=10, ipady=5)

b_down = Button(url_frame, padx=5,pady=5,text = "동영상 다운로드", command =url_download)
b_down.pack()

# 동영상 또는 mp3 선택 라디오버튼

Label(root, text="고화질 저화질  또는 Mp3").pack()

flty = StringVar()
btn1=Radiobutton(root, text="고화질",value="1", variable=flty)
btn1.select() # 기본값
btn2=Radiobutton(root, text="저화질",value="2", variable=flty)
btn3=Radiobutton(root, text="Mp3",value="3", variable=flty)

btn1.pack()
btn2.pack()
btn3.pack()

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# def btncmd():
   
#     print(flty.get())
    
# btn = Button(root, text="선택", command =btncmd)
# btn.pack()

root.mainloop()