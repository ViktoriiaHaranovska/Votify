from playwright.async_api import Page

class RegistrationPage:
    """Třída pro operace na registrační stránce."""
    def __init__(self, page: Page):
        self.page = page

    async def goto(self):
        """Naviguje na registrační stránku a čeká na její načtení."""
        await self.page.goto("https://auth.votify.app")
        await self.page.wait_for_load_state('networkidle')
        await self.page.wait_for_selector('input[name="email"]', state='visible')
        await self.page.wait_for_selector('input[name="password"]', state='visible')

    async def register(self, email: str, password: str):
        """Provádí registraci pomocí zadaného e-mailu a hesla."""
        await self.page.fill('input[name="email"]', email)
        await self.page.fill('input[name="password"]', password)
        await self.page.click('button[data-testid="submitAction"]')
        await self.page.wait_for_load_state('networkidle')

    async def is_error_message_visible(self) -> bool:
        """Kontroluje, zda je viditelné červené okno s chybovou zprávou."""
        try:
            await self.page.wait_for_selector('div[role="alert"]', state='visible', timeout=10000)
            return True
        except:
            return False

    async def get_error_message_text(self) -> str:
        """Získá text chybové zprávy."""
        error_element = await self.page.wait_for_selector('div[role="alert"]')
        return await error_element.inner_text()
