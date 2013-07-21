# -*- coding: utf-8 -*-
"""
Contains declaritive base for pydea
"""
import logging

from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__)

Base = declarative_base()
