from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'pydotdict'
LONG_DESCRIPTION = 'pydotdict is a python module that allows dot notation access / updating of a dictionary instance.'

# Setting up
setup(
        name="pydotdict",
        version=VERSION,
        author="Alex Redden",
        author_email="alexander.h.redden@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'dict','dot','dotdict','dot notation'],
        classifiers= []
)