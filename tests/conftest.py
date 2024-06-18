import pytest_asyncio
from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.registration_page import RegistrationPage


@pytest_asyncio.fixture(scope="function")
async def browser():
    """Fixture pro spuštění prohlížeče pomocí BasePage."""
    base_page = BasePage()
    await base_page.start()
    yield base_page.browser
    await base_page.close()

@pytest_asyncio.fixture(scope="function")
async def page(browser):
    """Fixture pro otevření nové stránky v prohlížeči."""
    page = await browser.new_page()
    yield page
    await page.close()

@pytest_asyncio.fixture(scope="function")
async def sign_in_page(page):
    """Fixture pro vytvoření instance SignInPage."""
    sign_in_page = SignInPage(page)
    yield sign_in_page

@pytest_asyncio.fixture(scope="function")
async def registration_page(page):
    """Fixture pro vytvoření instance RegistrationPage."""
    registration_page = RegistrationPage(page)
    yield registration_page
