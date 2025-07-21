import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import os

# === Chemin vers le fichier à uploader ===
chemin_fichier = r"C:\Users\thebe\OneDrive\www\code general\phyton\python-bot-montage-video\output\video_partie\Rick.and.Morty.S08E07.FRENCH.WEBRip.x264-Wawacity.zone\part_1.mp4"

# Vérifie si le fichier existe
if not os.path.exists(chemin_fichier):
    raise FileNotFoundError(f"Fichier non trouvé : {chemin_fichier}")

# === Configuration du profil Chrome ===
options = uc.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\thebe\Documents\chrome_profiles\tiktok_user")
options.add_argument("--profile-directory=Default")

# === Lancer le navigateur ===
driver = uc.Chrome(options=options)
driver.get("https://www.tiktok.com/tiktokstudio/upload?from=webapp")

# === Attendre que la page soit complètement chargée ===
time.sleep(5)

# === Trouver directement l'élément input type="file" ===
try:
    input_upload = driver.find_element(By.XPATH, '//input[@type="file"]')
    input_upload.send_keys(chemin_fichier)
    print("✅ Fichier envoyé avec succès !")
except Exception as e:
    print(f"❌ Erreur lors de l'envoi du fichier : {e}")

# Facultatif : attendre pour voir le résultat ou poursuivre d'autres automatisations
time.sleep(30)

input("Appuie sur Entrée pour fermer...")

driver.quit()
