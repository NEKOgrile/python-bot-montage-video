import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import os

# === Chemin vers le fichier vidéo à uploader ===
chemin_fichier = r"C:\Users\thebe\OneDrive\www\code general\phyton\python-bot-montage-video\output\video_partie\Rick.and.Morty.S08E07.FRENCH.WEBRip.x264-Wawacity.zone\part_1.mp4"

# === Vérifie que le fichier existe ===
if not os.path.exists(chemin_fichier):
    raise FileNotFoundError(f"❌ Fichier introuvable : {chemin_fichier}")

# === Configuration de Chrome avec le profil TikTok ===
options = uc.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\thebe\Documents\chrome_profiles")
options.add_argument("--profile-directory=Default")


# === Démarrer le navigateur avec undetected_chromedriver ===
try:
    driver = uc.Chrome(options=options)
    driver.get("https://www.tiktok.com/tiktokstudio/upload?from=webapp")
except Exception as e:
    raise RuntimeError(f"❌ Erreur au lancement du navigateur : {e}")

# === Attendre le chargement de la page ===
time.sleep(5)

# === Cherche le champ input de type "file" pour uploader ===
try:
    input_upload = driver.find_element(By.XPATH, '//input[@type="file"]')
    input_upload.send_keys(chemin_fichier)
    print("✅ Fichier envoyé avec succès !")
except Exception as e:
    print(f"❌ Erreur lors de l'envoi du fichier : {e}")

# === Pause pour voir le résultat / attendre chargement TikTok ===
time.sleep(30)

# === Fermer proprement ===
input("Appuie sur Entrée pour quitter...")
driver.quit()
