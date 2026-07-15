"""Small wrapper around pystata so init logic lives in one place."""

from c08_farming_exit.config import STATA_EDITION, STATA_PATH
import sys

def init_stata():
    """
    Initializes Stata. 

    As pystata is not pip-installed it cannot be installed using "uv add pystata". 
    Instead, it lives inside the Stata program folder. We need to add that folder 
    to sys.path before importing it. 
    Importantly, it can only be imported once per session. 
    This function takes care of it by remembering that it has already started Stata and 
    just does nothing at the second time. 
    """
    # checks if Stata program folder is already in sys.path
    if STATA_PATH not in sys.path:
        sys.path.append(STATA_PATH)

    import pystata
    pystata.config.init(STATA_EDITION)