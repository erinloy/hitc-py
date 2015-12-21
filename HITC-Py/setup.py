from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='HITC-Py',
      version=version,
      description="Python client for a running HITC API",
      long_description="""\
Python client for running HITC API""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='api',
      author='Jonathan Mackenzie',
      author_email='jonmac1@gmail.com',
      url='http://github.com/nupic-community/hitc-py',
      license='AGPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'requests'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
