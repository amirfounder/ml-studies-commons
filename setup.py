from setuptools import setup, find_packages

setup(
    name='commons',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'pdfkit==1.0.0',
    ]
)