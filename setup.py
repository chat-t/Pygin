"""Based on: https://github.com/pypa/sampleproject."""
from os import path
from setuptools import find_packages, setup

# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

TESTS_REQUIRE = ['pylint', 'pytest', 'pytest-pylint']
INSTALL_REQUIRE = ['pygame']

setup(
    name='pygame-engine',

    # Versions should comply with PEP440.
    version='0.0.3a',

    description='Simple pygame game engine.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/CarlosMatheus/Engine',

    author='Aloysio, Carlos, Igor',
    author_email='aloysiogl@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
    ],

    keywords='engine pygame',

    packages=find_packages(),

    install_requires=INSTALL_REQUIRE,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': TESTS_REQUIRE,
    },

    setup_requires=['pytest-runner'],

    tests_require=TESTS_REQUIRE,

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # for example: 'sample': ['package_data.dat']
    package_data={'requirements': ['requirements.txt']},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    project_urls={
        'Wiki': 'https://github.com/CarlosMatheus/Engine/wiki',
        'Source': 'https://github.com/CarlosMatheus/Engine',
    },
)
