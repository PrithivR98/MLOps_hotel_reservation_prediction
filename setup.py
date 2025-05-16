from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name = "First MLOPS Porject",
    version = "0.1",
    author = "Prithiv",
    packages = find_packages(),
    install_requires = requirements,
)