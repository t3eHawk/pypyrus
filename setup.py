import pypyrus
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

author = pypyrus.__author__
email = pypyrus.__email__
version = pypyrus.__version__
description = pypyrus.__doc__
license = pypyrus.__license__

setuptools.setup(
    name='pypyrus',
    version=version,
    author=author,
    author_email=email,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=license,
    url='https://github.com/t3eHawk/pypyrus',
    install_requires=[
        'pypyrus-logbook>=0.0.2', 'pypyrus-runner>=0.0.1',
        'pypyrus-etl>=0.0.1', 'pypyrus-tables>=0.0.2'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
