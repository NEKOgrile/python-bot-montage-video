
from moviepy.editor import VideoFileClip




def Get_Seconds_Video(title):

    clip = VideoFileClip(f"docs/video/{title}")
    seconds = clip.duration

    return seconds


def Number_Of_Part(total_duration_sec, duree_partie_sec):
 # Convertir en int la durée totale (arrondi à l'entier inférieur)
    total_duration_sec = int(total_duration_sec)
    duree_partie_sec = int(duree_partie_sec)

    n = total_duration_sec // duree_partie_sec  # nombre de parties complètes (int)
    r = total_duration_sec % duree_partie_sec   # reste en secondes (int)

    if r == 0:
        nombre_parties = n
        durees = [duree_partie_sec] * nombre_parties
    else:
        nombre_parties = n
        # Pour éviter un problème si nombre_parties == 0 (ex: durée < 120)
        if nombre_parties > 0:
            durees = [duree_partie_sec] * (nombre_parties - 1) + [duree_partie_sec + r]
        else:
            # cas où la vidéo dure moins de la durée d'une partie
            durees = [r]
            nombre_parties = 1

    return nombre_parties, durees