from settings.base import BASE_DIR
from django.utils.translation import gettext_lazy as _


LOCALE_PATHS = [
    BASE_DIR / "locale",
]

LANGUAGES = [
    ("uz", _("Uzbek (Latin)")),
    # ("uz_CYrl", _("Uzbek (Cyrillic)")),
    ("ru", _("Russian")),
    ("en", _("English")),
]

SESSION_LANGUAGE_KEY = "user_language"  # Key to store selected language

LANGUAGE_CODE = "en-us"
# LANGUAGE_CODE = "uz"
# LANGUAGE_CODE = "uz_CYrl"
# LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

# USE_L10N = True

USE_TZ = True
