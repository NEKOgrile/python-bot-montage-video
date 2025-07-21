# 🎬 Video Cutter & Formatter – Automatisation du montage vidéo  

Ce projet Python automatise le **formatage de vidéos longues en format vertical (ex. TikTok)**, en appliquant un fond flou, des textes dynamiques (saison, numéro de partie), puis en découpant automatiquement la vidéo en plusieurs segments.  

Il est pensé pour :  
- 🎥 Adapter facilement une vidéo à un format **1080x1920** (TikTok, Shorts…)  
- ✂️ **Découper automatiquement** une longue vidéo en parties définies  
- 🖼️ **Ajouter du texte dynamique** (saison, numéro de partie…)  


# 📌 Objectif  

Le script fonctionne en **deux étapes** :  

🔹 **Création d’une vidéo longue formatée** :  
- Redimensionne et centre la vidéo  
- Ajoute un fond flou  
- Ajoute un texte saison/épisode  

🔸 **Découpe automatique en plusieurs parties** :  
- Détermine automatiquement le nombre de parties  
- Crée des fichiers séparés `part_1.mp4`, `part_2.mp4`…  


# 📊 Ce que le programme fait  

✅ Analyse la durée de la vidéo originale  
✅ Crée une version longue adaptée aux réseaux sociaux  
✅ Découpe en plusieurs parties (ex. 2 min chacune, dernière partie ajustée)  
✅ Gère automatiquement les noms des fichiers générés  


# 🧱 Structure du projet  
```bash
┌── docs/  
│   └── video/  
│       ├── exemple_video_input.mp4  
│  
├── fonction/  
│   ├── cutting_Long_To_Short_Video.py    # Découpe la vidéo longue en parties  
│   ├── Make_Long_Video.py                # Crée la vidéo longue format TikTok  
│   ├── Number_Of_Part.py                 # Calcule le nombre de parties et durées  
│  
├── output/  
│   ├── video_longue/                     # Contient les versions longues formatées  
│   │   ├── exemple_video_entiere_output.mp4   
│   │  
│   └── video_partie/                     # Contient les parties découpées  
│       ├── exemple_video_parti1_output.mp4
│       ├── exemple_video_parti2_output.mp4
│       ├── exemple_video_parti3_output.mp4
│  
├── .gitignore  
├── cut.py                               # Script rapide de découpe  
└── main.py                              # Script principal (formatage + découpe)  

```
# 🧰 Prérequis  

Outil / Lib | Version recommandée | Utilisation  
--- | --- | ---  
Python | 3.10+ | Exécution des scripts  
pip | 23.x+ | Installation des dépendances  
MoviePy | 1.0.3+ | Manipulation vidéo  
OpenCV | 4.x | Effet flou sur fond vidéo  
ImageMagick | 7.1.2-0-Q16 | generation de textes 

💡 **ImageMagick** est requis pour MoviePy afin de générer des textes (`magick` doit être dans le PATH).  


# ⚙️ Installation rapide  

1️⃣ **Cloner le projet**  
git clone https://github.com/NEKOgrile/python-bot-montage-video.git  
cd video-cutter-formatter  

2️⃣ **Créer un environnement virtuel et installer les dépendances**  
python -m venv venv  
venv\Scripts\activate  # Windows  
pip install -r requirements.txt  

3️⃣ **Configurer ImageMagick**  
- Installer ImageMagick 7  
- Ajouter `magick` au PATH système  
- Vérifier avec `magick -version`  


# 🚀 Utilisation  

1️⃣ **Mettre les vidéos sources dans `docs/video/`**  

2️⃣ **Lancer le script principal**  
python main.py  

3️⃣ **Résultat automatique** :  
- Une version formatée dans `output/video_longue/<nom_video>/`  
- Les parties découpées dans `output/video_partie/<nom_video>/`  


# 🎯 Fonctionnement global  

- ✅ **Get_Seconds_Video** → récupère la durée de la vidéo  
- ✅ **Number_Of_Part** → calcule combien de parties et leurs durées  
- ✅ **Make_Long_Video** → crée une version TikTok avec fond flou + texte saison  
- ✅ **cutting_Long_To_Short_Video** → découpe en parties avec texte “Partie X”  


# 🧑‍💻 Auteur  

Projet développé par **Willem Cornil** pour automatiser le **formatage & découpe de vidéos**.  
N’hésitez pas à proposer des améliorations ou à contribuer via GitHub !  




maj : cree un ficher comme celui C:\Users\<votre nom>\Documents\chrome_profiles\tiktok_user pui dl chrome
