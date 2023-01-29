# Import moviepy editor library, which gives us the editing functions
from moviepy.editor import *

def read_input():
    opacities = []
    file = open("inputs.txt")
    contents = file.readlines()
    for i in range(len(contents)):
        placeholder = contents[i].rstrip()
        opacities.append(float(placeholder))
    file.seek(0)
    file.close()
    return opacities

videos = []
opacities = read_input()
for i in range(len(opacities)): 
    videos.append(VideoFileClip("video_" + str(i+1) + ".webm"))
    videos[i] = videos[i].set_opacity(opacities[i])

final_video = CompositeVideoClip(videos) 

final_video.write_videofile("final_video.webm")


