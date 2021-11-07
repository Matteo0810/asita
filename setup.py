from setuptools import setup, find_packages

setup(
    name="orbital",
    version="0.0.1",
    author="Mattéo Gaillard",
    description="A web application framework",
    long_description=open("README.md", "r", encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/Matteo0810/PyServ",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)