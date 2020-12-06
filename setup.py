"""
Flask-TGBot
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-TGBot',
    version='1.0',
    url='https://github.com/nextblu/flask_tgbot',
    license='MIT',
    author='nextblu',
    author_email='hello@netxblu.com',
    description='Very short description',
    long_description=__doc__,
    packages=['flask_tgbot'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)