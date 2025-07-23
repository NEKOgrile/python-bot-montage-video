import os

from fonction.Number_Of_Part import Get_Seconds_Video  , Number_Of_Part
from fonction.Make_Long_Video import Make_Long_Video
from fonction.cutting_Long_To_Short_Video import cutting_Long_To_Short_Video
from fonction.Get_Scheldule_Publish import best_posting_times
from fonction.Upload_Video_Part import Upload_Video_Part


title = "video_400s.mp4"
title_sans_ext = os.path.splitext(title)[0]


saison = "8"
episode = "9"

number_of_abonne = "190"
Goal = "500"


seconds = Get_Seconds_Video(title)

##temps de chaque partie en secondes
#
min_duration = 80
max_duration = 160
#
numberOfPart = Number_Of_Part(seconds ,min_duration , max_duration )
#
print(seconds)
print(numberOfPart)
print("soi : ", numberOfPart[0], "parties de 2 minutes et la dernière partie fait : ", numberOfPart[1][numberOfPart[0] - 1], "secondes")

#Make_Long_Video(title , saison , episode , number_of_abonne , Goal)
durations = numberOfPart[1]   # ← on garde la liste entière, ex: [120,120,160]
#cutting_Long_To_Short_Video(title , durations)

#jour = lundi = 0 dimache = 6 et 7 = ajoudui
#best_time_to_upload = (best_posting_times(f"output/video_partie/{title_sans_ext}" , 2))
#print(best_time_to_upload)
#Upload_Video_Part(title_sans_ext  , best_time_to_upload)    




#metre un temps aleatoir entre 63 et 136 sec soit 1munute3sec et 2munutes16sec
#publier tout les video avec un intervalle aleatoir entre 30 min et 1h15