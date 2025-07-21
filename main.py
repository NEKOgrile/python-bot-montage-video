import os

from fonction.Number_Of_Part import Get_Seconds_Video  , Number_Of_Part
from fonction.Make_Long_Video import Make_Long_Video
from fonction.cutting_Long_To_Short_Video import cutting_Long_To_Short_Video
from fonction.Get_Scheldule_Publish import best_posting_times
from fonction.Upload_Video_Part import open_tiktok


title = "Rick.and.Morty.S08E07.FRENCH.WEBRip.x264-Wawacity.zone.mp4"
title_sans_ext = os.path.splitext(title)[0]


saison = "8"
episode = "7"

seconds = Get_Seconds_Video(title)

#temps de chaque partie en secondes

#timeParPart = 120
#
#numberOfPart = Number_Of_Part(seconds , timeParPart)
#
#print(seconds)
#print(numberOfPart)
#print("soi : ", numberOfPart[0], "parties de 2 minutes et la dernière partie fait : ", numberOfPart[1][numberOfPart[0] - 1], "secondes")
#
#Make_Long_Video(title , saison , episode)
#durations = numberOfPart[1]   # ← on garde la liste entière, ex: [120,120,160]
#cutting_Long_To_Short_Video(title , durations)

#jour = lundi = 0 dimache = 6 et 7 = ajoudui
print(best_posting_times(f"output/video_partie/{title_sans_ext}" , 2))