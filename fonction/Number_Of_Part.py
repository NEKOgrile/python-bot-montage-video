import random
from moviepy.editor import VideoFileClip

def Get_Seconds_Video(title):
    clip = VideoFileClip(f"docs/video/{title}")
    seconds = clip.duration
    clip.close()
    return int(seconds)

def Number_Of_Part(total_duration_sec, min_duration=80, max_duration=160):
    total_duration_sec = int(total_duration_sec)
    durations = []
    remaining = total_duration_sec

    while remaining >= min_duration * 2:
        # on laisse assez pour une partie minimale à la fin
        max_possible = min(max_duration, remaining - min_duration)
        duration = random.randint(min_duration, max_possible)
        durations.append(duration)
        remaining -= duration

    # Gérer la dernière partie :
    if remaining >= min_duration:
        durations.append(remaining)
    else:
        if durations:
            durations[-1] += remaining  # fusion avec l'avant-dernière
        else:
            durations.append(remaining)  # cas extrême : vidéo très courte

    return len(durations), durations
