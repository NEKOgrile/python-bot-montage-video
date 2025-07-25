import cv2
import os
import random
from moviepy.editor import (
    VideoFileClip,
    CompositeVideoClip,
    TextClip,
    ColorClip,
    concatenate_videoclips
)
from moviepy.config import change_settings

# Utilisation d'ImageMagick (pour TextClip)
change_settings({"IMAGEMAGICK_BINARY": "magick"})

def flou_frame(frame):
    return cv2.GaussianBlur(frame, (51, 51), 30)

def Make_Long_Video(title, saison, episode, number_of_abonne, Goal):
    title_sans_ext = os.path.splitext(title)[0]
    output_dir = f"output/video_longue/{title_sans_ext}"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/{title_sans_ext}_longue.mp4"

    # Charger les vidéos
    clip = VideoFileClip(f"docs/video/{title}")
    clip_face = VideoFileClip("docs/face_came/Design sans titre (1).mp4")
    main_duration = clip.duration

    # --- Clip IA aléatoire ---
    ia_dir = "docs/ia_satifesent"
    ia_files = [f for f in os.listdir(ia_dir) if f.endswith((".mp4", ".mov", ".avi"))]
    if not ia_files:
        raise FileNotFoundError("Aucune vidéo IA trouvée dans le dossier.")

    # Sélection aléatoire et empilement jusqu'à couvrir toute la durée
    ia_clips = []
    total_duration = 0

    while total_duration < main_duration:
        ia_file = random.choice(ia_files)
        ia_part = VideoFileClip(os.path.join(ia_dir, ia_file)).volumex(0.2)  # 🔉 Baisse du volume IA ici
        ia_clips.append(ia_part)
        total_duration += ia_part.duration

    # Concaténer et couper à la durée exacte
    ia_clip = concatenate_videoclips(ia_clips).subclip(0, main_duration)

    # --- Ajustement durée pour face cam ---
    if clip_face.duration >= main_duration:
        clip_face = clip_face.subclip(0, main_duration)
    else:
        repeat_count = int(main_duration // clip_face.duration) + 1
        clip_face = concatenate_videoclips([clip_face] * repeat_count).subclip(0, main_duration)

    # --- Mise en forme des clips ---
    clip_face = clip_face.crop(y1=0, y2=600)
    clip_face = clip_face.resize(width=1080).set_position(("center", 0))

    zoomed = clip.resize(width=2000)
    clip_net = zoomed.crop(x_center=zoomed.w / 2, width=1080, height=clip.h).set_position(("center", "center"))

    ia_clip_resized = ia_clip.resize(width=1080).crop(y1=0, y2=540).set_position(("center", 1380))

    # --- Textes ---
    season_text = TextClip(
        f"saison {saison} : ep : {episode}",
        fontsize=70,
        color="white",
        font="Arial-Bold",
        stroke_color="black",
        stroke_width=2,
        size=(1080, None),
        method="caption"
    ).set_duration(main_duration).set_position(("center", 1300))

    bg = ColorClip(season_text.size, color=(0, 0, 0)).set_opacity(1).set_duration(main_duration).set_position(("center", 1300))

    abonnees_text = TextClip(
        f"objectif : {number_of_abonne} / {Goal} abonnés",
        fontsize=40,
        color="white",
        font="Arial-Bold",
        stroke_color="black",
        stroke_width=2,
        size=(1080, None),
        method="caption"
    ).set_duration(main_duration).set_position(("center", 1450))

    bg2 = ColorClip(abonnees_text.size, color=(0, 0, 0)).set_opacity(0.3).set_duration(main_duration).set_position(("center", 1450))

    # --- Composition finale ---
    final = CompositeVideoClip(
        [clip_net, ia_clip_resized, clip_face, bg, bg2, abonnees_text, season_text],
        size=(1080, 1920)
    )

    # Export
    final.write_videofile(output_path, codec="libx264", fps=30, threads=8)
