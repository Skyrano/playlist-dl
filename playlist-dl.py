import os
import sys

if len(sys.argv) == 1:
        playlist = "https://www.youtube.com/playlist?list=PLydQlw2Y-PCJBCyB9EvRrJR0ldcwG1_ML"
else:
        playlist = sys.argv[1]

exclude_list = {" lyrics"," lyric"," (lyrics)"," ENG Sub", " VIDEO", " Official", " (official music video)", " official",
                " (lyric)"," ENG SUB"," Subtitles", " [Lyrics]", " [ Lyrics ]", " MUSIC", " (official)", " (Official)",
                " Lyrics"," Lyric"," (Lyrics)"," (English Subtitles)", " (Official Music Video)", " (Music Video)",
                " (Lyric)"," English Subtitles"," (Subtitles)", " Music Video"}

def Clean(filename):
        filename = filename.replace("_", " ")
        filename = filename[0:-16] + filename[-4:]
        for word in exclude_list:
                filename = filename.replace(word, "") 
        return filename
        
os.chdir("/home/alistair/Musique/")
os.system("youtube-dl -x --audio-format mp3 --yes-playlist --download-archive /home/alistair/Musique/music-list --restrict-filenames {}".format(playlist))

for file in os.listdir("/home/alistair/Musique/"):
        if file.endswith(".mp3"):
                title = Clean(file)
                os.system("mv '/home/alistair/Musique/{}' '/home/alistair/Musique/ReadyToPhone/{}'".format(file,title))