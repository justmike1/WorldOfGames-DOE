#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='WorldOfGamesDEC',
    version='1.3.4',
    author='Mike Joseph',
    author_email='mikeyusufov@gmail.com',
    description='World of Games by Mike Joseph',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/justmike1/WorldOfGames-DEC',
    project_urls = {
        "Bug Tracker": "https://github.com/justmike1/WorldOfGames-DEC/issues"
    },
    license='MIT',
    packages=['WorldOfGamesDEC'],
    install_requires=['requests'],
    scripts=['bin/startWOG.py'],
)

