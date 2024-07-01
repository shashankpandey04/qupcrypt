
#### setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="qupcrypt",
    version="0.1.6",
    author="Shashank Pandey",
    author_email="jpshashank200@gmail.com",
    description="A custom encryption library using AES",
    long_description="A custom encryption library using AES and base64 encoding with Custom Algorithm for encryption and decryption. It is a simple and easy to use library for encryption and decryption of data. More Info: https://github.com/shashankpandey04/qupcrypt & https://sites.google.com/view/qupcrypt",
    long_description_content_type="text/markdown",
    url="https://github.com/shashankpandey04/qupcrypt",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pycryptodome",
    ],
)
