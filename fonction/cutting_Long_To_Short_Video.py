from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip , ColorClip
import os

def cutting_Long_To_Short_Video(title, time_list):
    title_sans_ext = os.path.splitext(title)[0]
    output_dir = f"output/video_partie/{title_sans_ext}"
    os.makedirs(output_dir, exist_ok=True)

    input_path = f"output/video_longue/{title_sans_ext}/{title_sans_ext}_longue.mp4"
    clip = VideoFileClip(os.path.abspath(input_path))
    dur = clip.duration
    print(f"Durée totale : {dur:.2f}s")

    start = 0
    for i, d in enumerate(time_list, start=1):
        end = min(start + d, dur)
        if start >= end:
            print("✅ Plus de segment à traiter.")
            break

        part_clip = clip.subclip(start, end)

        # Texte "Partie X"
        part_text = TextClip(
            f"Partie {i}",
            fontsize=60,
            color="white",
            font="Arial-Bold",
            stroke_color="black",
            stroke_width=3,
            size=(600, None),  # limite de largeur pour forcer à centrer
            method="caption"
        ).set_duration(part_clip.duration).set_position(("center", 500))

        # Fond noir derrière le texte (bendo)
        text_bg = ColorClip(
            size=(part_text.w + 60, part_text.h + 40),  # marge autour du texte
            color=(0, 0, 0)
        ).set_opacity(1).set_duration(part_clip.duration).set_position(("center", 490))

        # Composition finale avec bendo + texte
        final = CompositeVideoClip([part_clip, text_bg, part_text], size=(1080, 1920))

        out_path = f"{output_dir}/part_{i}.mp4"
        final.write_videofile(
            out_path,
            codec="libx264",
            fps=30,
            temp_audiofile='temp-audio.m4a',
            remove_temp=True,
            audio_codec='aac'
        )

        start = end

    clip.close()
