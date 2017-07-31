#!/usr/bin/env python3
from setuptools import setup

from emacs_bindings import __version__


try:
    import pypandoc
    import re
    long_description = pypandoc.convert("README.md", "rst")
    # remove raw html blocks, they're not supported on pypi
    long_description = re.sub("\s+\.\. raw:: html\s*.+? -->", "", long_description, count=2)
except:
    long_description = ""


setup(
    name="emacs-keys-everywhere",
    version=__version__,
    description="Enable Emacs style key bindings on the desktop.",
    long_description=long_description,
    url="https://github.com/rahiel/emacs-keys-everywhere",
    license="GPLv3+",

    py_modules=["emacs_bindings"],
    install_requires=[],
    entry_points={"console_scripts": ["emacs-keys-everywhere=emacs_bindings:main"]},

    author="Rahiel Kasim",
    author_email="rahielkasim@gmail.com",
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        # "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities"
    ],
    keywords="emacs key bindings keybindings"
)
