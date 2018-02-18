from moviepy.editor import VideoFileClip as vid 
from glob import glob
import numpy, pickle
filenames = glob("*.mp4")
for f in filenames:
	name = f[:-3] + "mp3"
	vid(f).audio.write_audiofile(name)

print("Lets git it")