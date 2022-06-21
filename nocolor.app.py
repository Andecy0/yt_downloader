from pytube import YouTube
import time
import os

def code():
    while True:
        print("\nYoutube video downloader by AlphaDev")
        print("https://github.com/AlphaDev00\n\n")
        flink = input("Enter The Link:  ")
        yt = YouTube(flink)
        print("Selected Video:  ", yt.title)
        answer = input("Do you really want to download this video?  (Y/N) :    ")
        if answer == "Y":
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.get_by_itag(22)
            print("The video has been downloaded successfully!:    ", yt.title,".mp4")
            stream.download()
            os._exit()
            break
        if answer == "N":
            print("Canceling operation please wait...\n")
            time.sleep(2)
            print("Successfully cancelled!")
            continue

code()
