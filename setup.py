# -*- encoding: utf-8 -*-
import os
from setuptools import setup, find_packages
import notify as app


install_requires = open('requirements.txt').read().splitlines()


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-notify-x",
    version=app.__version__,
    description='Notification sytem for Django',
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django notifications, notify, facebook like notifications',
    author='Soumik Dutta',
    author_email='shalearkane@gmail.com',
    url="https://github.com/shalearkane/django-notify-x",
    packages=find_packages(),
    package_data={'notify': ['static/notify/*js',
                             'templates/*.html',
                             'templates/notifications/*.html',
                             'templates/notifications/includes/*.html',
                             'templates/notifications/includes/*.js']},
    include_package_data=True,
    install_requires=install_requires,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 4.2',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
    ]
)
