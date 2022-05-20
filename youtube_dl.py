# youtube_dl 이용 다운로드

from cProfile import label
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import youtube_dl
import os
import subprocess

root = Tk()
root.title("Youtube DownLoader--by Dongeal Im")
root.geometry("640x480+300+100")
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
    os.chdir(folder_selected)

def url_download():
    url=url_name.get()
    yt_url=url.split('?')[0]
       
    if len(entry_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장경로를 선택하세요")
        return
    if len(url_name.get()) == 0:
        msgbox.showwarning("경고", "동영상 Url을 입력하세요")
        return    
    
    if flty.get() == "1":
        root.title("동영상 다운로드 중 ---")
        with youtube_dl.YoutubeDL() as ydl:
            ydl.download([yt_url])

    elif flty.get() == "2":
        root.title("mp3 다운로드 중 ---")
        ydl_opts = {
            'format': '251',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
        
        file_list = os.listdir('.')
        video = [file for file in file_list if file.endswith(".webm")]
        # 파일 하나하나 모두 mp3 로 변환한다.
        for v in video:
            # os.rename(v, v.split('.')[0]+'.mp3')
            os.rename(v, v.replace(".webm" , ".mp3"))
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

Label(root, text="동영상  또는 Mp3").pack()

flty = StringVar()
btn1=Radiobutton(root, text="동영상",value="1", variable=flty)
btn1.select() # 기본값

btn2=Radiobutton(root, text="Mp3",value="2", variable=flty)

btn1.pack()
btn2.pack()

# def btncmd():
   
#     print(flty.get())
    
# btn = Button(root, text="선택", command =btncmd)
# btn.pack()

root.mainloop()