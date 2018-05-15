# Delete this file after: https://github.com/sdispater/poetry/issues/34

import setuptools

setuptools.setup(
    packages=setuptools.find_packages(),

    entry_points={'console_scripts': [
        'coverage.space = coveragespace.cli:main',
    ]},
)
