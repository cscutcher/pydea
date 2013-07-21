# -*- coding: utf-8 -*-
"""
Contains code to start up sessions for models
"""
import logging

from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from pydea.models.base import Base

logger = logging.getLogger(__name__)


Session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
metadata = Base.metadata


def initialise(engine):
    """
    Provide additional config to session factory to allow it to start providing sessions
    """
    Session.configure(bind=engine)
    metadata.bind = engine
    metadata.create_all()
