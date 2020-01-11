import os
import sys

if len(sys.argv) == 1:
        playlist = "https://www.youtube.com/playlist?list=PLydQlw2Y-PCJBCyB9EvRrJR0ldcwG1_ML"
else:
        playlist = sys.argv[1]

#" Lyric"," lyric"," (Lyric)"," (official music video)"," (lyric)", " [Lyrics]"," [ Lyrics ]", " (official)", " (Official)"," (lyrics)"," (Lyrics)"," (English Subtitles)", " (Official Music Video)", " (Music Video)"," (Subtitles)",   
exclude_list = {" - Lyrics"," Lyrics"," lyrics"," ENG Sub", " VIDEO", " Official", " official",
                " ENG SUB"," Subtitles"," MUSIC"," English Subtitles"," Music Video"}

def Clean(filename):
        filename = filename.replace("_", " ")
        filename = filename[0:-16] + filename[-4:]
        for word in exclude_list:
                filename = filename.replace(word, "") 
                while filename[-5] in [" ","-","."]:
                        filename = filename[0:-5] + filename[-4:]
        return filename
        
os.chdir("/home/skyrano/Musique/")
os.system("youtube-dl -x --audio-format mp3 --yes-playlist --download-archive /home/skyrano/Musique/music-list --restrict-filenames {}".format(playlist))

for file in os.listdir("/home/skyrano/Musique/"):
        if file.endswith(".mp3"):
                title = Clean(file)
                os.system("mv '/home/skyrano/Musique/{}' '/home/skyrano/Musique/ReadyToPhone/{}'".format(file,title))
