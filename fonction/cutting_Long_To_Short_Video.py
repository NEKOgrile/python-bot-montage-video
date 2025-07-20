from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip
import os

def cutting_Long_To_Short_Video(title, time):

    # ✅ Nom sans extension (ex: video_400s)
    title_sans_ext = os.path.splitext(title)[0]

    # ✅ Dossier où seront sauvées les parties
    output_dir = f"output/video_partie/{title_sans_ext}"
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Nouveau chemin correct pour la version longue
    input_path = f"output/video_longue/{title_sans_ext}/{title_sans_ext}_longue.mp4"

    # ✅ Charger la version longue
    clip = VideoFileClip(os.path.abspath(input_path))

    start = 0

    for i, d in enumerate(time, start=1):
        end = start + d
        part_clip = clip.subclip(start, end)

        # ✅ Texte
        part_text = TextClip(
            f"Partie {i}",
            fontsize=70,
            color="white",
            font="Arial-Bold",
            stroke_color="black",
            stroke_width=3  # contour plus épais
        ).set_duration(part_clip.duration)


        # On place le texte centré, un peu plus bas
        part_text = part_text.set_position(("center", 500))  # 1400 px du haut → un peu au bas de l’écran


        # ✅ Combinaison finale
        final = CompositeVideoClip([part_clip, part_text])

        # ✅ Sauvegarder la partie découpée
        final.write_videofile(f"{output_dir}/part_{i}.mp4", codec="libx264", fps=30)

        start = end
