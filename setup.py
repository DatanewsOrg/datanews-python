from setuptools import setup
from setuptools import find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(
    name='datanews',
    version="0.0.5",
    author="Vladyslav Mokrousov",
    author_email="mokrousov@datanews.io",
    description="Python client library for Datanews API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DatanewsOrg/datanews-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=required
)
