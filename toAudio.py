from moviepy.editor import VideoFileClip as vid 
from glob import glob

files = glob("*.mp4")

for f in files:
	name = f[:-3] + "mp3"
	vid(f).audio.write_audiofile(name)