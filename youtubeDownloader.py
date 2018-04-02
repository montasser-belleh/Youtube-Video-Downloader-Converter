
# coding: utf-8

# In[1]:


import pytube
import os
from moviepy.editor import *


# In[2]:


def videoFromLink(link):
    
    path = os.getcwd()
    yt = pytube.YouTube(link)
    video_list = yt.get_videos()
    i = 0
    for vid in (video_list):
        print(str(i)," : ",str(vid))
        i+=1
    vid_id = int(input("choose a quality : \n"))
    vid = video_list[vid_id]
    vid.download(path)

def youtubeToMp3(video):
    
    clip = VideoFileClip(video)
    audio = video.split(sep="/")[-1].split(sep=".")[0]+".mp3"
    clip.audio.write_audiofile(audio)


# In[9]:


def main():
    
    cond ='y'
    while cond == 'y':
        video_to_download = input("Give youtube link : ")
        videoFromLink(video_to_download)
        test = input("do you want to convert it to mp3? [y/n]")
        if test == 'y':
            video_name = input("give the video name as saved :")
            youtubeToMp3(video_name)
        elif test == 'n':
            continue
        else:
            print("Wrong Choice , please answer y/n")
        cond = input("Do you want to do this again? [y/n]")
    
    


# In[10]:


if __name__=='__main__' :
    main()

