# -*- coding: utf-8 -*-
"""
Contains the majority of models for pydea
"""
import logging
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import Unicode
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from apex.models import AuthUser

from pydea.models.base import Base

logger = logging.getLogger(__name__)



#authorship_table = Table("authorship",
#                         Base.metadata,
#                         Column("idea_id", Integer, ForeignKey("ideas.id")),
#                         Column("profile_id", Integer, ForeignKey("profiles.id")))
#

class Idea(Base):
    __tablename__ = 'ideas'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
#    authors = relationship("ExtendedProfile",
#                           secondary=authorship_table,
#                           backref="ideas")
#

class ExtendedProfile(AuthUser):
    __tablename__ = "profiles"
    __mapper_args__ = {'polymorphic_identity': 'profile'}
    id = Column(Integer, ForeignKey('auth_users.id'), primary_key=True)
    first_name = Column(Unicode(80))
    last_name = Column(Unicode(80))
    available_votes = Column(Integer())
