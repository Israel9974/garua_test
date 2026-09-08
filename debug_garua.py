import logging
logging.basicConfig(level=logging.INFO)

import sys
from zendriver import Config
from garua.exceptions import BrowserNotFoundError
import garua.scraping.browser as browser_mod
import garua.scraping.scraper as scraper_mod

def patched_get_browser_config():
    check = browser_mod.check_browser()
    if not check.ok or not check.path:
        raise BrowserNotFoundError(check.message)
    return Config(browser_executable_path=check.path, sandbox=False)

# Reemplazamos la función en ambos lugares donde Garúa la usa
browser_mod.get_browser_config = patched_get_browser_config
scraper_mod.get_browser_config = patched_get_browser_config

from garua.main import cli
sys.exit(cli())
