from moviepy.editor import VideoFileClip

# Charger la vidéo d'origine
clip = VideoFileClip("docs/video/Rick.and.Morty.S08E01.FRENCH.WEBRip.x264-Wawacity.pictures.mp4")

# Couper pour ne garder que les 10 premières secondes
clip_10s = clip.subclip(3, 13)

# Sauvegarder la vidéo coupée
clip_10s.write_videofile("video_10s.mp4", codec="libx264", fps=30)
