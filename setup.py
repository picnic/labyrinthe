import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="labyrinthe",
    version="0.1",
    author="Pierre-Nicolas Tollitte",
    author_email="pierrenicolas.tollitte@gmail.com",
    description="Bibliothèque pour concevoir des exercices pour apprendre la programmation avec Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/picnic/labyrinthe",
    packages=setuptools.find_packages(),
    test_suite='tests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
