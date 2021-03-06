from distribute_setup import use_setuptools
use_setuptools()

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'apex',
    'docopt',
    'paste',
    'WebError',
    'repoze.tm2',
]

setup(
    name='pydea',
    version='0.0',
    description='pydea',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web wsgi bfg pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='pydea',
    install_requires=requires,
    entry_points={
        "paste.app_factory": "main=pydea:wsgi_factory",
        "console_scripts": ["initialise_pydea_db=pydea.scripts.initialise_db:main"]
    },
)
