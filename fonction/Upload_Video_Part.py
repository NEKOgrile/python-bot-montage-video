import undetected_chromedriver as uc

options = uc.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\thebe\Documents\chrome_profiles\tiktok_user")
options.add_argument("--profile-directory=Default")

driver = uc.Chrome(options=options)
driver.get("https://www.tiktok.com/tiktokstudio/upload?from=webapp")

input("Appuie sur Entrée pour fermer...")
driver.quit()
