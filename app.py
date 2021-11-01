from pytube import YouTube
from tkinter import *
import time
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()

def code():
    while True:
        print(Fore.MAGENTA)
        print("\nYoutube video downloader by AlphaDev")
        print("https://github.com/AlphaDev00\n\n")
        print(Style.RESET_ALL)
        flink = input(Fore.BLUE + "Enter The Link:  " + Style.RESET_ALL)
        yt = YouTube(flink)
        print(Fore.GREEN + "Selected Video:  ", yt.title + Style.RESET_ALL)
        answer = input(Fore.RED + "Do you really want to download this video?  (Y/N) :    " + Style.RESET_ALL)
        if answer == "Y":
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.get_by_itag(22)
            print(Fore.GREEN + "The video has been downloaded successfully!:    ", yt.title,".mp4")
            stream.download()
            os._exit()
            break
        if answer == "N":
            print(Fore.GREEN + "Canceling operation please wait...\n")
            time.sleep(2)
            print(Fore.GREEN + "Successfully cancelled!")
            continue

code()


'''
window = Tk()
window.resizable(False, False)
window.title("Youtube Downloader")
window.config(bg="gray")
window.configure(width=490, height=400)



entry = Entry(window)
entry.place(x="140",y="150",width=200,height=30)

mainloop()
'''