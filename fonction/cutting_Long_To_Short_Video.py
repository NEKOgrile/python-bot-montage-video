from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
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
            print("✅ Plus de segment à traiter, on sort.")
            break

        part_clip = clip.subclip(start, end)

        part_text = TextClip(
            f"Partie {i}",
            fontsize=60,
            color="white",
            font="Arial-Bold",
            stroke_color="black",
            stroke_width=3
        ).set_duration(part_clip.duration).set_position(("center", 590))

        final = CompositeVideoClip([part_clip, part_text])

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
