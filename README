# 🎬 Video Cutter & Formatter – Automatisation du montage vidéo  

Ce projet Python automatise le **formatage de vidéos longues en format vertical (ex. TikTok)**, en appliquant un fond flou, des textes dynamiques (saison, numéro de partie), puis en découpant automatiquement la vidéo en plusieurs segments.  

Il est pensé pour :  
- 🎥 Adapter facilement une vidéo à un format **1080x1920** (TikTok, Shorts…)  
- ✂️ **Découper automatiquement** une longue vidéo en parties définies  
- 🖼️ **Ajouter du texte dynamique** (saison, numéro de partie…)  

```bash
# 📌 Objectif  
```bash
Le script fonctionne en **deux étapes** :  

🔹 **Création d’une vidéo longue formatée** :  
- Redimensionne et centre la vidéo  
- Ajoute un fond flou  
- Ajoute un texte saison/épisode  

🔸 **Découpe automatique en plusieurs parties** :  
- Détermine automatiquement le nombre de parties  
- Crée des fichiers séparés `part_1.mp4`, `part_2.mp4`…  

```bash
# 📊 Ce que le programme fait  
```bash
✅ Analyse la durée de la vidéo originale  
✅ Crée une version longue adaptée aux réseaux sociaux  
✅ Découpe en plusieurs parties (ex. 2 min chacune, dernière partie ajustée)  
✅ Gère automatiquement les noms des fichiers générés  

```bash
# 🧱 Structure du projet  
```bash
┌── docs/  
│   └── video/  
│       ├── Rick.and.Morty.S08E01.FRENCH.WEBRip.x264-Wawacity.pictures.mp4  
│       ├── Rick.and.Morty.S08E08.FRENCH.WEBRip.x264-Wawacity.motorcycles.mp4  
│       ├── video_10s.mp4  
│       ├── video_200s.mp4  
│       └── video_400s.mp4  
│  
├── fonction/  
│   ├── cutting_Long_To_Short_Video.py    # Découpe la vidéo longue en parties  
│   ├── Make_Long_Video.py                # Crée la vidéo longue format TikTok  
│   ├── Number_Of_Part.py                 # Calcule le nombre de parties et durées  
│   └── __pycache__/                      # Cache Python compilé  
│  
├── output/  
│   ├── video_longue/                     # Contient les versions longues formatées  
│   │   ├── Rick.and.Morty.S08E08.FRENCH.WEBRip.x264-Wawacity.motorcycles/  
│   │   ├── video_10s/  
│   │   ├── video_200s/  
│   │   └── video_400s/  
│   │  
│   └── video_partie/                     # Contient les parties découpées  
│       ├── Rick.and.Morty.S08E08.FRENCH.WEBRip.x264-Wawacity.motorcycles/  
│       ├── video_10s/  
│       └── video_400s/  
│  
├── .gitignore  
├── cut.py                               # Script rapide de découpe  
└── main.py                              # Script principal (formatage + découpe)  

```bash
# 🧰 Prérequis  
```bash
Outil / Lib | Version recommandée | Utilisation  
--- | --- | ---  
Python | 3.10+ | Exécution des scripts  
pip | 23.x+ | Installation des dépendances  
MoviePy | 1.0.3+ | Manipulation vidéo  
OpenCV | 4.x | Effet flou sur fond vidéo  

💡 **ImageMagick** est requis pour MoviePy afin de générer des textes (`magick` doit être dans le PATH).  

```bash
# ⚙️ Installation rapide  
```bash
1️⃣ **Cloner le projet**  
git clone https://github.com/ton-profil/video-cutter-formatter.git  
cd video-cutter-formatter  

2️⃣ **Créer un environnement virtuel et installer les dépendances**  
python -m venv venv  
venv\Scripts\activate  # Windows  
pip install -r requirements.txt  

3️⃣ **Configurer ImageMagick**  
- Installer ImageMagick 7  
- Ajouter `magick` au PATH système  
- Vérifier avec `magick -version`  

```bash
# 🚀 Utilisation  
```bash
1️⃣ **Mettre les vidéos sources dans `docs/video/`**  

2️⃣ **Lancer le script principal**  
python main.py  

3️⃣ **Résultat automatique** :  
- Une version formatée dans `output/video_longue/<nom_video>/`  
- Les parties découpées dans `output/video_partie/<nom_video>/`  

```bash
# 🎯 Fonctionnement global  
```bash
- ✅ **Get_Seconds_Video** → récupère la durée de la vidéo  
- ✅ **Number_Of_Part** → calcule combien de parties et leurs durées  
- ✅ **Make_Long_Video** → crée une version TikTok avec fond flou + texte saison  
- ✅ **cutting_Long_To_Short_Video** → découpe en parties avec texte “Partie X”  

```bash
# 🛣️ Roadmap (prochaines étapes)  
```bash
💡 Ajouter un mode batch (traiter toutes les vidéos d’un dossier automatiquement)  
📈 Paramétrage interactif (durée par partie, style du texte, etc.)  
🎥 Génération automatique de preview (image miniature par partie)  
🔁 Support multi-format (YouTube Shorts, Insta Reels…)  

```bash
# 🧑‍💻 Auteur  
```bash
Projet développé par **Ton Nom/Pseudo** pour automatiser le **formatage & découpe de vidéos**.  
N’hésitez pas à proposer des améliorations ou à contribuer via GitHub !  
```bash

👉 Donc **partout où normalement il y aurait eu des `bash`, j’ai mis `bash`** sans les retirer.  

Veux-tu que je **fasse ça sur tout le README complet d’un coup** dans un seul bloc ? Ou bien je garde ce format multi-blocs ?
