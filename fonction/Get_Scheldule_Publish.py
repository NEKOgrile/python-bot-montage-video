import os
import re
from datetime import datetime, timedelta
import pytz

# Créneaux horaires fixes en heure locale Europe/Paris
SLOTS = ["10:00", "11:00", "12:00", "14:00", "15:00", "17:00", "18:00", "20:00", "21:00"]  # ex.

JOURS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

def Poste_Video_Part(folder_path):
    files = os.listdir(folder_path)
    parts = [f for f in files if re.match(r"part_\d+\.mp4", f)]
    return sorted(parts, key=lambda f: int(re.search(r"part_(\d+)", f).group(1)))

def best_posting_times(folder_path, force_day=None):
    videos = Poste_Video_Part(folder_path)
    n = len(videos)
    if n == 0:
        return []

    tz = pytz.timezone("Europe/Paris")
    today = datetime.now(tz).date()

    if isinstance(force_day, int) and 0 <= force_day < 7:
        offset = (force_day - today.weekday()) % 7
        start_date = today + timedelta(days=offset)
    else:
        start_date = today

    result = []
    max_per_day = len(SLOTS)
    # on veut max 2 jours
    total_days = min(2, (n + max_per_day - 1) // max_per_day)

    idx = 0
    for day_index in range(total_days):
        slots_to_use = min(max_per_day, n - idx)
        for slot_index in range(slots_to_use):
            vid = videos[idx]
            pub_date = start_date + timedelta(days=day_index)
            time_str = SLOTS[slot_index]
            hour, minute = map(int, time_str.split(':'))
            pub_dt = datetime(pub_date.year, pub_date.month, pub_date.day,
                              hour, minute, tzinfo=tz)

            result.append((
                vid,
                pub_dt.strftime("%H:%M"),
                JOURS[pub_dt.weekday()],
                pub_dt.strftime("%d"),
                pub_dt.strftime("%m")
            ))
            print(f"{vid} → {time_str} le {JOURS[pub_dt.weekday()]} {pub_dt.strftime('%d')}/{pub_dt.strftime('%m')}")
            idx += 1
            if idx >= n:
                break
        if idx >= n:
            break

    return result
