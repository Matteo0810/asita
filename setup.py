from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="asita",
    version="0.1.0",
    author="Mattéo Gaillard",
    description="A web application framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matteo0810/PyServ",
    packages=[
        "asita",
        "asita.handlers",
        "asita.utils"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)