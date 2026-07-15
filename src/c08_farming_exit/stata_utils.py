"""Small wrapper around pystata so init logic lives in one place."""

from c08_farming_exit.config import STATA_EDITION

def init_stata():
    import sys
    sys.path.append(r"C:\Program Files\Stata18\utilities")
    import pystata
    pystata.config.init(STATA_EDITION)