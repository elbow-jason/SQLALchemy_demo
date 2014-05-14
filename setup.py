from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import sqla_demo

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.txt', 'CHANGES.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='sqla_demo',
    version=sqla_demo.__version__,
    url='http://github.com/jlgoldb2/SQLAlchemy_demo/',
    license='MIT License',
    author='Jason Goldberger',
    tests_require=['pytest'],
    install_requires=['SQLAlchemy==0.9.4'
                    ],
    cmdclass={'test': PyTest},
    author_email='jlgoldb2@asu.edu',
    description='a simple demonstration for using postgreSQL via SQLAlchemy ORM',
    long_description=long_description,
    packages=['sqla_demo'],
    include_package_data=True,
    platforms='any',
    test_suite='sqla_demo.test.test_sqla_demo',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)