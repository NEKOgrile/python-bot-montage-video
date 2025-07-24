import cv2
import os
from moviepy.editor import (
    VideoFileClip,
    CompositeVideoClip,
    TextClip,
    ColorClip,
    ImageClip,
)
from moviepy.config import change_settings
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.speedx import speedx
from moviepy.editor import concatenate_videoclips


# Utilisation d'ImageMagick (nécessaire pour TextClip avec méthode "caption")
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

    # Ajuster durée de la face cam
    main_duration = clip.duration
    face_duration = clip_face.duration

    if face_duration >= main_duration:
        clip_face = clip_face.subclip(0, main_duration)
    else:
        repeat_count = int(main_duration // face_duration) + 1
        clip_face = concatenate_videoclips([clip_face] * repeat_count).subclip(0, main_duration)


    # Rogner la vidéo face pour mieux cadrer le visage (plus haut que 50)
    clip_face = clip_face.crop(y1=0, y2=600)
    clip_face = clip_face.resize(width=1080).set_position(("center", 0))


    # Image de fond floutée (1 seule frame traitée)
    # Créer fond flouté dynamique à partir du clip redimensionné
    clip_bg = clip.resize(height=1920).fl_image(flou_frame)


    # Redimensionner sans zoom ni recadrage
    clip_net = clip.resize(width=1100).set_position(("center", "center"))
    # Texte saison/épisode (petit et centré bas)
    season_text = TextClip(
        f"saison {saison} : ep : {episode}",
        fontsize=70,
        color="white",
        font="Arial-Bold",
        stroke_color="black",
        stroke_width=2,
        size=(1080, None),
        method="caption"
    ).set_duration(clip.duration).set_position(("center", 1300))

    bg = ColorClip(season_text.size, color=(0, 0, 0)).set_opacity(0.6).set_duration(clip.duration).set_position(("center", 1300))

    # Texte abonnés (en haut)
    abonnees_text = TextClip(
        f"objectif : {number_of_abonne} / {Goal} abonnés",
        fontsize=40,
        color="white",
        font="Arial-Bold",
        stroke_color="black",
        stroke_width=2,
        size=(1080, None),
        method="caption"
    ).set_duration(clip.duration).set_position(("center", 1450))

    bg2 = ColorClip(abonnees_text.size, color=(0, 0, 0)).set_opacity(0.3).set_duration(clip.duration).set_position(("center", 1450))

    # Composition finale
    final = CompositeVideoClip(
        [clip_bg, clip_net, bg, bg2, abonnees_text, season_text, clip_face],
        size=(1080, 1920)
    )

    # Export
    final.write_videofile(output_path, codec="libx264", fps=30, threads=8)
