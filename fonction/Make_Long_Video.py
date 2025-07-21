import cv2
import os
from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip
from moviepy.config import change_settings



# Force MoviePy à utiliser 'magick' (nouveau nom d'ImageMagick 7)
change_settings({"IMAGEMAGICK_BINARY": "magick"})


def flou_frame(frame):
    return cv2.GaussianBlur(frame, (51, 51), 30)


def Make_Long_Video(title , saison , episode):
    # ✅ Extraire le nom sans extension (ex: "video_10s")
    title_sans_ext = os.path.splitext(title)[0]

    # ✅ Créer le dossier de sortie unique
    output_dir = f"output/video_longue/{title_sans_ext}"
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Nom du fichier final (même nom que l’original)
    output_path = f"{output_dir}/{title_sans_ext}_longue.mp4"
    # Charger la vidéo avec une f-string

    clip = VideoFileClip(f"docs/video/{title}")

    # Dimensions TikTok
    tiktok_width = 1080
    tiktok_height = 1920

    # ✅ Fond flou
    clip_bg = clip.resize(height=tiktok_height)
    clip_bg = clip_bg.fl_image(flou_frame)

    # ✅ Vidéo nette un peu plus grande
    clip_net = clip.resize(width=1100).set_position(("center", "center"))

    # ✅ Texte
    season_text = TextClip(
        f"Season{saison} ep {episode}",
        fontsize=70,
        color="white",
        font="Arial-Bold",
        stroke_color="black",
        stroke_width=3  # contour plus épais
    ).set_duration(clip.duration)


    # On place le texte centré, un peu plus bas
    season_text = season_text.set_position(("center", 1300))  # 1400 px du haut → un peu au bas de l’écran


    # ✅ Combinaison finale
    final = CompositeVideoClip([clip_bg, clip_net, season_text], size=(tiktok_width, tiktok_height))

    # ✅ Exporter la vidéo finale dans son dossier dédié
    final.write_videofile(output_path, codec="libx264", fps=30)