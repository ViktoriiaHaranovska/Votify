# **Votify** - Automatizované Testy


_Tento projekt obsahuje automatizované testy pro Votify.
Testy jsou napsány v jazyce Python s použitím frameworku Playwright a pytest._

# ****Nastavení a Instalace****

### Předpoklady

Python 3.7 nebo vyšší


Nainstalovaný Google Chrome nebo Chromium



**Struktura Souborů**

* _**config/config.py**_
Obsahuje přihlašovací údaje, které jsou použity v testech.

* _**modules/ui/page_objects/base_page.py**_
Třída BasePage obsahuje základní operace s prohlížečem pomocí Playwright.

* **_modules/ui/page_objects/registration_page.py_**
Třída RegistrationPage obsahuje operace na registrační stránce.

* **_modules/ui/page_objects/sign_in_page.py_**
Třída SignInPage obsahuje operace na přihlašovací stránce.

* **_tests/ui/test_navigation.py_**
Testuje navigaci mezi stránkami po přihlášení.

* **_tests/ui/test_registration.py_**
Testuje registraci s neplatným heslem a kontroluje zobrazení chybového hlášení.

* **_tests/ui/test_sign_in.py_**
Testuje přihlášení pomocí stránky SignInPage.

* **_tests/conftest.py_**
Obsahuje fixture pro inicializaci prohlížeče a stránky, a pro vytvoření instancí SignInPage a RegistrationPage.

* **_tests/test_base_page.py_**
Základní test pro ověření načítání stránky pomocí Playwright.

* **_pytest.ini_**
Konfigurace pro pytest, obsahuje definice markerů pro různé typy testů


# Závěr


Tento projekt poskytuje základ pro automatizaci testů  Votify pomocí Playwright a pytest. Pokud máte jakékoliv dotazy nebo potřebujete pomoc, neváhejte se obrátit na autora projektu.