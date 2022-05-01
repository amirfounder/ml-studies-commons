from setuptools import setup, find_packages

setup(
    name='commons',
    version='0.0.4',
    packages=find_packages(),
    install_requires=[
        'daos @ git+https://github.com/amirfounder/ml-studies-daos',
    ]
)