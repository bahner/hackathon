import os
from setuptools import setup
def read(fname):
    """Read myself"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='lships',
    version='0.0.1',
    author='Lars Bahner',
    author_email='lars.bahner@gmail.com',
    description='A modern scalable version of Battleships for Microbit LED-displays.',
    license='GPL-3',
    keywords='k12 education game network',
    url='https://github.com/bahner/hackathon',
    packages=['lships',],
    long_description = 'README.md',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Games',
        'License :: OSI Aproved :: GPL-3,'
    ]
)
