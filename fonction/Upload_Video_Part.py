import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import pyautogui
import time
import os

from datetime import datetime

def selectionner_date(driver, jour_voulu, mois_voulu):
    """
    Sélectionne une date spécifique dans le calendrier TikTok Studio.
    Format attendu : jour_voulu = "21", mois_voulu = "07"
    """
    try:
        # Attendre que le calendrier soit bien visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tux-calendar"))
        )
        print("📅 Calendrier chargé.")

        mois_noms = {
            "janvier": "01", "février": "02", "mars": "03", "avril": "04",
            "mai": "05", "juin": "06", "juillet": "07", "août": "08",
            "septembre": "09", "octobre": "10", "novembre": "11", "décembre": "12"
        }

        # Lire le mois actuellement affiché
        en_tete = driver.find_element(By.XPATH, '//div[contains(@class,"tux-calendar-header")]')
        texte_mois_annee = en_tete.text.strip().lower()
        mois_actuel_nom, annee_actuelle = texte_mois_annee.split()

        mois_actuel = mois_noms.get(mois_actuel_nom)
        if not mois_actuel:
            print(f"❌ Mois non reconnu : {mois_actuel_nom}")
            return

        ecart = int(mois_voulu) - int(mois_actuel)
        if ecart != 0:
            bouton = en_tete.find_elements(By.TAG_NAME, "button")[1 if ecart > 0 else 0]
            for _ in range(abs(ecart)):
                bouton.click()
                time.sleep(0.5)

        # Attente explicite que les jours soient présents
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//td[@role="gridcell"]/div'))
        )

        jours = driver.find_elements(By.XPATH, '//td[@role="gridcell"]/div')
        for jour in jours:
            if jour.text.strip() == str(int(jour_voulu)):  # Ex: "7" == "07"
                jour.click()
                print(f"✅ Jour {jour_voulu} sélectionné.")
                return

        print(f"❌ Jour {jour_voulu} non trouvé.")
    except Exception as e:
        print(f"❌ Erreur sélection date : {e}")




def scroll_jusqua_et_selectionne_heure(driver, heure_voulue=None, scroll_amount=23):
    """
    Scrolle de manière simple vers le bas 'scroll_amount' fois (par défaut 23 crans),
    attend 50 secondes, puis fait un break.
    """
    print(heure_voulue)
    try:
        print(f"🔽 Scroll de {scroll_amount} crans vers le bas en cours...")
        for i in range(scroll_amount):
            pyautogui.scroll(500)  # Scroll vers le haut
            time.sleep(0.01)
            print(f"↘️ Scroll {i + 1}/{scroll_amount}")

        scroll_depth = int(heure_voulue)
        for i in range(scroll_depth):
            pyautogui.scroll(-500)
            time.sleep(0.01)
            print(f"↘️ Scroll {i + 1}/{scroll_depth}")


        print("🛑 Fin du scroll simulé. (Pas de sélection d'heure)")
        return True  # Toujours vrai, car plus de recherche d'heure
    except Exception as e:
        print(f"❌ Erreur pendant le scroll simulé : {e}")
        return False




def move_mouse_above_element(driver, element, y_offset=30):
    """Déplace la souris au-dessus d’un élément (en y_offset)."""
    try:
        location = element.location_once_scrolled_into_view
        size = element.size
        x = location['x'] + size['width'] // 2
        y = location['y'] + size['height'] // 2 - y_offset

        window_position = driver.get_window_position()
        x += window_position['x']
        y += window_position['y'] + 80  # Ajustement pour la barre de titre

        pyautogui.moveTo(x, y, duration=0.3)
        time.sleep(0.3)
        print(f"✅ Souris déplacée vers x={x}, y={y}")
    except Exception as e:
        print(f"❌ Erreur déplacement souris : {e}")


def Upload_Video_Part(path, best_time_to_upload):
    options = uc.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:\Users\thebe\Documents\chrome_profiles")
    options.add_argument("--profile-directory=Default")
    # 👇 Ajoute ceci avec le chemin exact vers ton Chrome
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    
    try:
        driver = uc.Chrome(options=options)
        driver.get("https://www.tiktok.com/tiktokstudio/upload?from=webapp")
    except Exception as e:
        raise RuntimeError(f"❌ Erreur au lancement du navigateur : {e}")

    time.sleep(5)
    wait = WebDriverWait(driver, 10)

    for index, (nom_fichier, heure_minute, jour, numero_jour, numero_mois) in enumerate(best_time_to_upload, start=1):
        try:
            heure, minute = heure_minute.split(":")
        except Exception as e:
            print(f"❌ Format heure incorrect '{heure_minute}' : {e}")
            continue

        chemin_fichier = os.path.abspath(f"output/video_partie/{path}/{nom_fichier}")
        print(f"\n⏳ Partie {index}/{len(best_time_to_upload)} : {nom_fichier} pour {jour} à {heure_minute}")

        if not os.path.exists(chemin_fichier):
            print(f"❌ Fichier introuvable : {chemin_fichier}")
            continue

        try:
            input_upload = driver.find_element(By.XPATH, '//input[@type="file"]')
            input_upload.send_keys(chemin_fichier)
            print(f"✅ {nom_fichier} envoyé avec succès.")
        except Exception as e:
            print(f"❌ Erreur upload : {e}")
            continue

        try:
            time.sleep(0.5)
            champ_description = driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")
            champ_description.click()
            time.sleep(1)
            champ_description.send_keys(Keys.CONTROL, 'a')
            champ_description.send_keys(Keys.BACKSPACE)
            time.sleep(0.5)

            numero_partie = nom_fichier.replace(".mp4", "").replace("part_", "")
            description = f"""part {numero_partie}
#sérieaddict #binge #momentfort
#partie{numero_partie} #épisode{numero_partie}
#scèneculte #film #serie
#suspens #intrigue #mustwatch
#foryou #pourtoi #tiktokserie
#saison8 #rickandmorty @fa17ur3"""
            champ_description.send_keys(description)
            print("✅ Description insérée.")
            time.sleep(0.5)
        except Exception as e:
            print(f"❌ Erreur description : {e}")

        try:
            bouton_programmer = driver.find_element(By.XPATH, '//span[text()="Programmer"]')
            bouton_programmer.click()
            print("✅ Bouton 'Programmer' cliqué.")
        except Exception as e:
            print(f"❌ Erreur clic 'Programmer' : {e}")
            continue

        # Sélection de l'heure et des minutes après clic
        try:
            champ_heure = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.TUXTextInputCore-input')))
            ActionChains(driver).move_to_element(champ_heure).click().perform()
            print("✅ Sélecteur heure/minute affiché.")
            time.sleep(1.2)

            move_mouse_above_element(driver, champ_heure, y_offset=30)
            print("✅ Souris positionnée au-dessus du champ.")
            time.sleep(1)

            heure_ok = scroll_jusqua_et_selectionne_heure(driver, heure)
            elements = driver.find_elements(By.XPATH, '//div[contains(@class,"tiktok-timepicker-option-list")]//div[contains(@class,"tiktok-timepicker-option-item")]//div[contains(@class,"tiktok-timepicker-option-item")]')
            print("🔍 Vérification des minutes affichées :")
            for el in elements:
                texte = el.text.strip()
                print(f"➡️ '{texte}'")

            

            if heure_ok:
                print(f"✅ {heure}:{minute} sélectionné avec succès.")
            else:
                print(f"⚠️ Échec de sélection pour {heure}:{minute}.")

            # Déplacement simulé de la souris vers la droite
            try:
                x, y = pyautogui.position()
                print(f"📍 Position actuelle de la souris : x={x}, y={y}")
                for i in range(1, 11):
                    pyautogui.moveTo(x + (5 * i), y, duration=0.02)
                print(f"✅ Souris déplacée progressivement de 50px vers la droite.")
            except Exception as e:
                print(f"❌ Erreur lors du déplacement simulé de la souris : {e}")

            # Scroll vers le haut de 16 crans
            try:
                print("🔄 Début du scroll vers le haut (12 crans)...")
                for i in range(12):
                    pyautogui.scroll(100)  # Scroll de 1 cran vers le haut
                    time.sleep(0.01)       # Pause visible entre chaque scroll (modifiable)
                    print(f"↥ Scroll {i+1}/16 effectué.")
                print("✅ Scroll de 16 crans vers le haut terminé.")
            except Exception as e:
                print(f"❌ Erreur lors du scroll progressif : {e}")
            # Scroll vers le bas en fonction des minutes
            try:
                minute_int = int(minute)
                scroll_count = minute_int // 5  # 1 scroll pour chaque tranche de 5 minutes
                print(f"🕒 Minute = {minute_int}, donc on va scroller vers le bas {scroll_count} fois.")

                for i in range(scroll_count):
                    pyautogui.scroll(-100)  # Scroll vers le bas
                    time.sleep(0.01)
                    print(f"↘️ Scroll bas {i+1}/{scroll_count}")
                print("✅ Scroll minute terminé.")
            except Exception as e:
                print(f"❌ Erreur lors du scroll minute : {e}")

        except Exception as e:
            print(f"❌ Erreur lors de la sélection heure/minute : {e}")


        # Fermer le sélecteur d'heure (en cliquant en dehors)
        pyautogui.click(x=500, y=300)  # Coordonnées génériques à ajuster si besoin
        time.sleep(0.5)


        try:
            # Attente que le champ de date soit cliquable
            champ_date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.TUXTextInputCore-input[readonly][value*="2025"]'))
            )

            champ_date.click()
            print("🖱️ Champ de date cliqué.")

            time.sleep(1.5)  # Attendre l'apparition du calendrier

            try:
                print("🔍 Recherche des jours visibles dans le calendrier...")

                # Trouver tous les <span> qui ont une classe contenant "day"
                jours = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//span[contains(@class, "day")]'))
                )

                print(f"📅 {len(jours)} jours détectés :")
                for i, jour in enumerate(jours, start=1):
                    texte = jour.text.strip()
                    classes = jour.get_attribute("class")
                    print(f"  ➤ Jour {i}: '{texte}' (classes: {classes})")

                # 🎯 Jour ciblé à partir de ta donnée [('part_1.mp4', '16:00', 'Mardi', '22', '07')]
                jour_trouve = False

                for jour in jours:
                    texte = jour.text.strip()
                    classes = jour.get_attribute("class")

                    # On clique uniquement sur les jours valides
                    if texte == numero_jour and "valid" in classes:
                        print(f"🖱️ Clic sur le jour {texte} (classes: {classes})")
                        jour.click()
                        jour_trouve = True
                        break

                if not jour_trouve:
                    print(f"⚠️ Le jour '{numero_jour}' n'a pas été trouvé ou n'est pas cliquable.")

            except Exception as e:
                print(f"❌ Erreur affichage des jours : {e}")

        except Exception as e:
            print(f"❌ Erreur lors du clic ou sélection de la date : {e}")

        try:
            # Attente que le bouton "Programmer" soit cliquable
            bouton_programmer = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-e2e="post_video_button"]'))
            )
            bouton_programmer.click()
            print("✅ Bouton 'Programmer' cliqué avec succès.")
        except Exception as e:
            print(f"❌ Erreur lors du clic sur le bouton 'Programmer' : {e}")

        time.sleep(2)


        try:
            # Aller vers l'URL TikTok Studio sans relancer le navigateur
            driver.get("https://www.tiktok.com/tiktokstudio/upload?from=webapp")
            print("🔄 Navigation vers la page d'upload réussie.")
            time.sleep(4)  # Attendre le chargement complet de la page
        except Exception as e:
            print(f"❌ Erreur navigation vers la page d'upload : {e}")



    time.sleep(10)


    input("\n✅ Tous les fichiers traités. Appuie sur Entrée pour quitter...")

    
    driver.quit()
