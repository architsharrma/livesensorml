from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirements_list: List[str] = []
    with open('requirements.txt') as f:
        requirements_list = [line.strip() for line in f if line.strip() and not line.strip().startswith('-e')]
    return requirements_list

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Archit",
    author_email = "archit192000@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)

