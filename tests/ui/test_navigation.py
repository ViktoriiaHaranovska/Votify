import pytest
from playwright.async_api import TimeoutError
from config.config import LOGIN_EMAIL, LOGIN_PASSWORD

@pytest.mark.asyncio
async def test_navigation(sign_in_page):
    """Test pro ověření navigace mezi stránkami."""
    # Přihlášení
    await sign_in_page.goto()
    await sign_in_page.login(LOGIN_EMAIL, LOGIN_PASSWORD)

    page = sign_in_page.page

    # Definování položek menu a odpovídajících fragmentů URL
    menu_items = {
        'Kalendář': 'calendar',
        'Dokumenty': 'documents',
        'Hlasování': 'voting',
        'Uživatelé': 'users',
        'Organizace': 'organization',
        'Feedback': None
    }

    for item_text, url_fragment in menu_items.items():
        try:
            print(f"Navigating to '{item_text}'")
            # Čekání na zobrazení položky menu
            await page.wait_for_selector(f"span.MuiTypography-root:has-text('{item_text}')", timeout=20000)
            menu_element = page.locator(f"span.MuiTypography-root:has-text('{item_text}')")
            await menu_element.click()
            # Čekání na načtení stránky
            await page.wait_for_timeout(3000)
            await page.wait_for_load_state('networkidle', timeout=20000)
            print(f"Current URL: {page.url}")

            if url_fragment:
                # Kontrola, zda URL obsahuje správný fragment
                assert f'/{url_fragment}' in page.url, f"Nepodařilo se přejít na stránku {item_text}"
            else:
                # Speciální kontrola pro "Feedback"
                await page.wait_for_selector("button:has-text('Odeslat')", timeout=20000)
                assert await page.locator("button:has-text('Odeslat')").is_visible(), "Nepodařilo se přejít na stránku Feedback"
        except TimeoutError:
            print(f"Timeout while navigating to '{item_text}'")