import logging
import sys

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")

from garua.main import cli

sys.exit(cli())
