import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='WorldOfGames-DEC',
    version='1.0.0',
    author='Mike Joseph',
    author_email='mikeyusufov@gmail.com',
    description='Installing World Of Games, a project from DevOps Experts College',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/justmike1/WorldOfGames-DEC',
    project_urls = {
        "Bug Tracker": "https://github.com/justmike1/WorldOfGames-DEC/issues"
    },
    license='MIT',
    packages=['WorldOfGames-DEC'],
    install_requires=['requests'],
)

