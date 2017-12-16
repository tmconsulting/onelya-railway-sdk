from setuptools import setup, find_packages
from onelya_railway_sdk.api import __version__


setup(
    version=__version__,
    name='onelya_railway_sdk',
    packages=find_packages(),

    install_requires=[
        'requests'
    ],

    description='Onelya Python SDK',

    author='Travel Managment Consulting',
    author_email='otd@tm-consulting.ru',

    url='https://github.com/tmconsulting/onelya-railway-sdk',
    download_url='https://github.com/tmconsulting/onelya-railway-sdk/archive/%s.tar.gz' % __version__,

    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)