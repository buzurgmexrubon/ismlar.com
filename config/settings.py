from settings.base import *
from settings.installed_apps import *
from settings.middlewares import *
from settings.templates import *
from settings.password_validation import *
from settings.internationalization import *
from settings.static_files import *

IS_DEVELOPMENT = os.getenv("IS_DEVELOPMENT", False)

if IS_DEVELOPMENT:
    try:
        from settings.development import *
    except ImportError:
        pass
else:
    try:
        from settings.production import *
    except ImportError:
        pass
