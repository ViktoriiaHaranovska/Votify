from playwright.async_api import Page

class SignInPage:
    """Třída pro operace na stránce přihlášení."""
    def __init__(self, page: Page):
        self.page = page

    async def goto(self):
        """Naviguje na přihlašovací stránku a čeká na její načtení."""
        await self.page.goto("https://auth.votify.app")
        await self.page.wait_for_load_state('networkidle')
        await self.page.wait_for_selector('input[name="email"]', state='visible')
        await self.page.wait_for_selector('input[name="password"]', state='visible')

    async def login(self, email: str, password: str):
        """Provádí přihlášení pomocí zadaného e-mailu a hesla."""
        await self.page.fill('input[name="email"]', email)
        await self.page.fill('input[name="password"]', password)
        await self.page.wait_for_selector('button[data-testid="submitAction"]', state='visible')

        # Získání a zobrazení hodnot pro kontrolu
        email_value = await self.page.input_value('input[name="email"]')
        password_value = await self.page.input_value('input[name="password"]')
        print(f"Email Value: {email_value}, Password Value: {password_value}")

        await self.page.click('button[data-testid="submitAction"]')
        await self.page.wait_for_load_state('networkidle')
        await self.page.wait_for_url('https://app.votify.app/cs*')
