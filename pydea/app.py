# -*- coding: utf-8 -*-
"""
Creats main Pydea WSGI App
"""
import logging

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pydea.models import initialise

logger = logging.getLogger(__name__)


def wsgi_factory(global_config, **settings):
    """
    This returns the Pydea WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialise(engine)

    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.include('apex', route_prefix='/auth')
    config.scan()
    return config.make_wsgi_app()
