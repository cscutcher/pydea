# -*- coding: utf-8 -*-
"""
Initialise the DB for Pydea
Usage:
    initialise_db.py <config-path>

"""
import logging
import sys

from docopt import docopt
from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings
from pyramid.paster import setup_logging

import pydea.models

logger = logging.getLogger(__name__)


def main(argv=sys.argv[1:]):
    options = docopt(__doc__, argv=argv)
    config_uri = options["<config-path>"]

    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')

    pydea.models.initialise(engine)
