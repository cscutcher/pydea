import unittest
from pyramid import testing
from pydea.models import initialise


class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        initialise(engine)

    def tearDown(self):
        testing.tearDown()
