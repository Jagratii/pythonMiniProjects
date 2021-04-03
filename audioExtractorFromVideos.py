from moviepy import editor

video = moviepy.editor.VideoFileClip('vid.mp4')

audio = video.audio

audio.write_audiofile('vid.mp3')