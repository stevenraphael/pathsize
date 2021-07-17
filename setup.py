from setuptools import setup

setup(
    name="pathsize",
    version='1.0',
    description="Lists the sizes of items in a directory",
    author="Steven Raphael",
    author_email="stevennraphael@gmail.com",
    url="https://github.com/stevenraphael/pathsize",
    license="MIT",
    py_modules=['main'],
    install_requires=[
        'docopt',
    ],
    entry_points={
        'console_scripts': [
            'pathsize = main:main',
        ],
    },
)
