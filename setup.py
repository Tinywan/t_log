#!/usr/bin/python3
import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="t_log",
    version="0.51",
    author="Tinywan",
    author_email="756684177@qq.com",
    description="A small log package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tinywan/t_log",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
