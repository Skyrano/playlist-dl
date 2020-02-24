import os
import sys

if len(sys.argv) == 1:
        playlist = "https://www.youtube.com/playlist?list=PLydQlw2Y-PCJBCyB9EvRrJR0ldcwG1_ML"
else:
        playlist = sys.argv[1]

exclude_list = {" Lyrics"," lyrics"," ENG Sub", " VIDEO", " Official", " official",
                " ENG SUB"," Subtitles"," MUSIC"," English Subtitles"," Music Video"}

def Clean(filename):
        filename = filename.replace("_", " ")
        filename = filename[0:-16] + filename[-4:]
        for word in exclude_list:
                filename = filename.replace(word, "") 
                while filename[-5] in [" ","-","."]:
                        filename = filename[0:-5] + filename[-4:]
        return filename
        
os.chdir("/data/data/com.termux/files/home/storage/shared/Documents/playlist-dl/music_dir/")
os.system("youtube-dl -x --audio-format mp3 --yes-playlist --download-archive /data/data/com.termux/files/home/storage/shared/Documents/playlist-dl/music_dir/music-list --restrict-filenames {}".format(playlist))

for file in os.listdir("/data/data/com.termux/files/home/storage/shared/Documents/playlist-dl/music_dir/"):
        if file.endswith(".mp3"):
                title = Clean(file)
                os.system("mv '/data/data/com.termux/files/home/storage/shared/Documents/playlist-dl/music_dir/{}' '/data/data/com.termux/files/home/storage/shared/Music/{}'".format(file,title))
