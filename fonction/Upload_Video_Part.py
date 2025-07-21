from playwright.sync_api import sync_playwright

def open_tiktok():
    with sync_playwright() as p:
        # Lance Chrome en mode non-headless (fenêtre visible)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        
        # Nouvelle page
        page = context.new_page()
        
        # Va sur TikTok
        page.goto("https://www.tiktok.com")

        # Pause pour garder la fenêtre ouverte (interagir à la main)
        print("Navigateur ouvert sur TikTok. Appuie sur Entrée pour quitter...")
        input()

        # Ferme tout
        browser.close()

if __name__ == "__main__":
    open_tiktok()
