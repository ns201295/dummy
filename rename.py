import google.cloud.vision as gcv
from moviepy.editor import VideoFileClip
import io, os 
from glob import glob
from nltk.corpus import words

client 	= gcv.ImageAnnotatorClient()
screenshot_dir = 'Frames'

def image_to_text(image_path):

	file 	 = io.open(image_path,"rb").read()
	image 	 = gcv.types.Image(content=file)
	response = client.document_text_detection(image=image)

	return response.full_text_annotation.text


def video_to_image_samples(video_path, sample_time_in_seconds=10):

	directory = screenshot_dir + "/" + video_path.replace(" ","_").replace(".","_")

	if not os.path.exists(directory):
		os.makedirs(directory)
		print("Making directory :",directory)

	video = VideoFileClip(video_path)

	for time in range(sample_time_in_seconds,int(video.duration),sample_time_in_seconds):
		video.save_frame(directory+"/"+str(time)+".png",t=time)
		print("Saving Frame : " + directory+"/"+str(time)+".png")

	video.reader.close()
	video.audio.reader.close_proc()

	return directory 


def main():

	if not os.path.exists(screenshot_dir):
		os.makedirs(screenshot_dir)
		print("Making directory : ",screenshot_dir)

	videos = glob("*.mp4")
	videos.sort()

	for video in videos:
		print("Video = " + video)
		directory =  video_to_image_samples(video)
		frames = list(os.walk(directory))[0][2]

		temp = []
		for i in frames:
			temp.append(int(i.split('.')[0]))
		temp.sort()
		frames = []
		for i in temp:
			frames.append(str(i)+".png")

		text = []
		print("Converting image to text")
		for frame in frames:
			try:
				response = str(image_to_text(directory+'/'+frame)).lower().split()
				print(str(response))
				for word in response:
					if word in words.words():
						text.append(word)
			except:pass
		unique = []
		_ = [unique.append(x.title()) for x in text if x.title() not in unique]

		print("Text Found = ",str(unique))

		command = 'rename "' + video + '" "' + video.split(".")[0] + ". " + " ".join(unique) + '.mp4"'
		print(command)
		os.system('rename "' + video + '" "' + video.split(".")[0] + ". " + " ".join(unique) + '.mp4"')

		print("\n\n")
		

if __name__ == '__main__':
	main()









