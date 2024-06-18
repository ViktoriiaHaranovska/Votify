import pytest
from config.config import LOGIN_EMAIL, LOGIN_PASSWORD

@pytest.mark.prihlaseni
@pytest.mark.asyncio
async def test_sign_in(sign_in_page):
    """Test pro ověření přihlášení pomocí stránky SignInPage."""
    await sign_in_page.goto()
    await sign_in_page.login(LOGIN_EMAIL, LOGIN_PASSWORD)

    current_url = sign_in_page.page.url
    print(f"Current URL: {current_url}")

    assert current_url.startswith("https://app.votify.app/cs"), f"Unexpected URL: {current_url}"
