from setuptools import setup,find_packages

with open (file="requirements.txt") as f:
    requirements=f.read().splitlines()

setup(
    name="MLOps-Project1",version="0.1",author="Kiran",packages=find_packages(),
    install_requires=requirements
)