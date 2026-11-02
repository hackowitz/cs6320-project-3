#!/usr/bin/env python

"""Setup for the CS 6320 Project 3 starter package."""

from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="CS6320-Fall2026-Proj3",
    version="2.0.0",
    description=("CS 6320 Project 3: Camera Projection Matrix and "
                 "Fundamental Matrix Estimation"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="University of Utah, CS 6320",
    license="MIT",
    classifiers=[
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="computer-vision",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.9",
)
