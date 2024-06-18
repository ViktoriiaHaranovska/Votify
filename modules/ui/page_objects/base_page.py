from playwright.async_api import async_playwright, Browser, Page

class BasePage:
    """Třída pro základní operace s prohlížečem pomocí Playwright."""
    def __init__(self, browser_type='chromium'):
        """Inicializuje třídu s daným typem prohlížeče (výchozí je 'chromium')."""
        self.browser_type = browser_type
        self.browser: Browser = None
        self.page: Page = None
        self.playwright = None

    async def start(self):
        """Spustí Playwright a otevře novou stránku v prohlížeči."""
        self.playwright = await async_playwright().start()
        browser_launcher = getattr(self.playwright, self.browser_type)
        self.browser = await browser_launcher.launch(headless=False)  # Додавання headless=False для зручності налагодження
        self.page = await self.browser.new_page()

    async def close(self):
        """Zavře stránku, prohlížeč a zastaví Playwright."""
        if self.page:
            await self.page.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()