import os               # Module pour manipuler les fichiers et dossiers
import re               # Module pour les expressions régulières (regex)
from datetime import datetime, timedelta  # Gestion des dates et durées
import pytz             # Gestion des fuseaux horaires
import math             # Fonctions mathématiques (ex: ceil)

# Dictionnaire des plages horaires en UTC par jour de la semaine (0 = lundi, ..., 6 = dimanche)
heure_de_pointe_utc = {
    0: ("12:00", "14:00"),  # Lundi
    1: ("15:00", "17:00"),  # Mardi
    2: ("11:00", "13:00"),  # Mercredi
    3: ("16:00", "18:00"),  # Jeudi
    4: ("10:00", "12:00"),  # Vendredi
    5: ("14:00", "16:00"),  # Samedi
    6: ("13:00", "15:00"),  # Dimanche
}

jours_semaine_str = {
    0: "Lundi",
    1: "Mardi",
    2: "Mercredi",
    3: "Jeudi",
    4: "Vendredi",
    5: "Samedi",
    6: "Dimanche"
}


# Fonction qui liste les fichiers vidéo "part_X.mp4" dans un dossier donné
def Poste_Video_Part(folder_path):
    files = os.listdir(folder_path)  # Liste tous les fichiers dans le dossier
    # Filtre les fichiers correspondant au pattern "part_X.mp4" où X est un nombre
    part_files = [f for f in files if re.match(r"part_\d+\.mp4", f)]
    # Trie la liste des fichiers par numéro (ex: part_1 avant part_2)
    sorted_parts = sorted(part_files, key=lambda f: int(re.search(r"part_(\d+)", f).group(1)))
    return sorted_parts  # Retourne la liste triée

# Fonction qui génère un planning de publication basé sur une heure médiane
def generate_schedule(mid_time_str, num_videos, interval_minutes=30):
    mid_time = datetime.strptime(mid_time_str, "%H:%M").time()  # Convertit "HH:MM" en objet time
    today = datetime.now(pytz.utc).date()  # Date actuelle UTC (sans heure)
    # Combine la date d'aujourd'hui avec l'heure médiane, et fixe le fuseau UTC
    mid_datetime = datetime.combine(today, mid_time).replace(tzinfo=pytz.utc)

    middle_index = math.ceil(num_videos / 2)  # Indice vidéo médiane (ex: 6 si 11 vidéos)

    schedule = []
    for i in range(1, num_videos + 1):
        diff = (middle_index - i) * interval_minutes  # Décalage en minutes par rapport au milieu
        scheduled_time = mid_datetime - timedelta(minutes=diff)  # Calcule l'heure de publication
        schedule.append(scheduled_time)  # Ajoute à la liste du planning
    return schedule  # Retourne la liste des heures programmées

# Fonction principale qui calcule le meilleur planning de publication selon le jour actuel
def best_posting_times(folder_path, force_day=7):
    """
    Calcule le planning de publication des vidéos avec jour et heure.
    
    force_day : entier entre 0 et 6 pour forcer un jour (0=lundi, ..., 6=dimanche)
                7 (par défaut) pour prendre le jour actuel automatiquement.
                
    Retourne une liste de tuples : (nom_video, heure_HH:MM, jour_en_clair)
    """
    jours_semaine_str = {
        0: "Lundi",
        1: "Mardi",
        2: "Mercredi",
        3: "Jeudi",
        4: "Vendredi",
        5: "Samedi",
        6: "Dimanche"
    }

    # Choix du jour (forcé ou actuel)
    if force_day in range(0, 7):
        jour = force_day
    else:
        now_utc = datetime.now(pytz.utc)
        jour = now_utc.weekday()

    jour_str = jours_semaine_str.get(jour, "Jour inconnu")

    # Récupérer la plage horaire du jour choisi
    start_str, end_str = heure_de_pointe_utc.get(jour, ("12:00", "14:00"))

    # Calculer l'heure médiane (milieu de la plage)
    start_dt = datetime.strptime(start_str, "%H:%M")
    end_dt = datetime.strptime(end_str, "%H:%M")
    mid_minutes = (start_dt.hour * 60 + start_dt.minute + end_dt.hour * 60 + end_dt.minute) // 2
    mid_hour = mid_minutes // 60
    mid_minute = mid_minutes % 60
    mid_time_str = f"{mid_hour:02d}:{mid_minute:02d}"

    videos = Poste_Video_Part(folder_path)
    num_videos = len(videos)

    # Générer le planning des heures de publication
    schedule = generate_schedule(mid_time_str, num_videos, interval_minutes=30)

    simple_list = []
    for video, dt in zip(videos, schedule):
        heure_str = dt.strftime("%H:%M")
        print(f"{video} → {heure_str} ({jour_str})")
        simple_list.append((video, heure_str, jour_str))

    return simple_list
