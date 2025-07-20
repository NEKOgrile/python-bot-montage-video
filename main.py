from fonction.Number_Of_Part import Get_Seconds_Video  , Number_Of_Part
from fonction.Make_Long_Video import Make_Long_Video
from fonction.cutting_Long_To_Short_Video import cutting_Long_To_Short_Video


title = "Rick.and.Morty.S08E08.FRENCH.WEBRip.x264-Wawacity.motorcycles.mp4"

seconds = Get_Seconds_Video(title)

#temps de chaque partie en secondes

timeParPart = 120

numberOfPart = Number_Of_Part(seconds , timeParPart)

print(seconds)
print(numberOfPart)
print("soi : ", numberOfPart[0], "parties de 2 minutes et la dernière partie fait : ", numberOfPart[1][numberOfPart[0] - 1], "secondes")

Make_Long_Video(title)
durations = numberOfPart[1]   # ← on garde la liste entière, ex: [120,120,160]
cutting_Long_To_Short_Video(title , durations)