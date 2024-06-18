import pytest
from config.config import LOGIN_EMAIL

@pytest.mark.asyncio
async def test_invalid_password(registration_page):
    """Test pro ověření chybového hlášení při nesprávném zadání hesla."""
    await registration_page.goto()

    invalid_data = {
        "email": LOGIN_EMAIL,
        "password": "wrongpassword"
    }

    await registration_page.register(invalid_data["email"], invalid_data["password"])
    try:
        print(f"Checking for error message visibility")
        is_visible = await registration_page.is_error_message_visible()
        assert is_visible, "Expected error message to be visible, but it was not."

        error_message = await registration_page.get_error_message_text()
        print(f"Error message found: {error_message}")
        assert "heslo" in error_message.lower() or "password" in error_message.lower(), f"Expected error message to contain 'heslo' or 'password', but got: {error_message}"
    except Exception as e:
        assert False, f"Error message not found or other error: {str(e)}"
