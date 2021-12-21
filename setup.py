from setuptools import setup, find_packages
from pathlib import Path
VERSION = "0.0.4"
DESCRIPTION = "pydotted"
this_directory = Path(__file__).parent
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()# Setting up
setup(
    name="pydotted",
    version=VERSION,
    author="Alex Redden",
    author_email="alexander.h.redden@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/aredden/pydotted.git",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[],
    keywords=["python", "dict", "dot", "dotdict", "dot notation", "pydotted"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
