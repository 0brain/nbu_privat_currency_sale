from setuptools import setup, find_packages

VERSION = '0.0.5'

with open("README.md", "r") as f:
    long_description = f.read()

DESCRIPTION = ('A library for getting currency sale rates of National Bank of Ukraine '
               'and PrivatBank, compare it graphically by currency selection during '
               'preset date range.')

setup(
    name="nbu_privat_currency_sale",
    version=VERSION,
    author="Nazar Khort",
    author_email="nazar.khort@gmail.com",
    license='MIT',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=find_packages(exclude=("tests",)),
    install_requires=['requests==2.27.1', 'matplotlib==3.5.1'],
    setup_requires=['wheel'],

    keywords=['python', 'exchange rate', 'privatbank', 'NBU', 'currency sale',
              'National Bank of Ukraine', 'compare currency', 'course change chart',
              'exchange rate chart', 'banks exchange rate', 'compare banks exchange rate'],
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Source': 'https://github.com/0brain/nbu_privat_currency_sale',
    },
)
