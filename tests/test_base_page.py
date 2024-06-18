import pytest

@pytest.mark.zakladni
@pytest.mark.asyncio
async def test_basic():
    """Základní test pro ověření načítání stránky pomocí Playwright."""
    from playwright.async_api import async_playwright

    # Spuštění Playwright v asynchronním kontextu
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://example.com')
        assert 'Example Domain' in await page.title()
        await browser.close()
