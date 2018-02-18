from moviepy.editor import VideoFileClip as video 
from glob import glob
import numpy

filenames = glob("*.mp4")

for f in filenames:
	name = f[:-3] + "mp3"
	video(f).audio.write_audiofile(name)