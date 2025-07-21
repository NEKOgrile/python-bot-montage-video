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


def scroll_avec_souris(amount=-5000, pause=0.2):
    """Simule un scroll souris vers le bas (amount négatif)."""
    try:
        pyautogui.scroll(amount)
        time.sleep(pause)
        print(f"✅ Scroll souris effectué (amount={amount})")
    except Exception as e:
        print(f"❌ Erreur scroll souris : {e}")


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

    try:
        driver = uc.Chrome(options=options)
        driver.get("https://www.tiktok.com/tiktokstudio/upload?from=webapp")
    except Exception as e:
        raise RuntimeError(f"❌ Erreur au lancement du navigateur : {e}")

    time.sleep(5)
    wait = WebDriverWait(driver, 10)

    for index, (nom_fichier, heure_minute, jour) in enumerate(best_time_to_upload, start=1):
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
            time.sleep(3)
            champ_description = driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")
            champ_description.click()
            time.sleep(1)
            champ_description.send_keys(Keys.CONTROL, 'a')
            champ_description.send_keys(Keys.BACKSPACE)
            time.sleep(0.5)

            numero_partie = nom_fichier.replace(".mp4", "").replace("part_", "")
            description = f"""part {numero_partie}
#ricketmorty
#partie{numero_partie}
#suite
#pourtoii
#serie
#saison8 @fa17ur3"""
            champ_description.send_keys(description)
            print("✅ Description insérée.")
        except Exception as e:
            print(f"❌ Erreur description : {e}")

        try:
            bouton_programmer = driver.find_element(By.XPATH, '//span[text()="Programmer"]')
            bouton_programmer.click()
            print("✅ Bouton 'Programmer' cliqué.")
        except Exception as e:
            print(f"❌ Erreur clic 'Programmer' : {e}")
            continue

    # Sélection de l'heure
    try:
        champ_heure = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.TUXTextInputCore-input')))
        ActionChains(driver).move_to_element(champ_heure).click().perform()
        print("✅ Sélecteur heure/minute affiché.")
        time.sleep(1.2)

        move_mouse_above_element(driver, champ_heure, y_offset=30)
        print("✅ Souris positionnée au-dessus du champ.")

        time.sleep(1)
        scroll_avec_souris(amount=-5000)  # Scroll fort vers le bas

    except Exception as e:
        print(f"❌ Erreur lors de la sélection de l'heure : {e}")

    input("\n✅ Tous les fichiers traités. Appuie sur Entrée pour quitter...")
    driver.quit()
