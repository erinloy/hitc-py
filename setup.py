try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version_dict = {}
execfile('hitcpy/version.py', {}, version_dict)
version = version_dict['version']

def findRequirements():
  """
  Read the requirements.txt file and parse into requirements for setup's
  install_requirements option.
  """
  return [
    line.strip()
    for line in open("requirements.txt").readlines()
    if not line.startswith("#")
  ]

setup(name='hitcpy',
      version=version,
      description="Python client for a running HITC API",
      long_description="""\
Python client for running HITC API""",
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python'],
      keywords=['htm', 'api', 'rest', 'nupic', 'client'],
      author='Jonathan Mackenzie',
      author_email='jonmac1@gmail.com',
      url='http://github.com/nupic-community/hitc-py',
      license='AGPLv3',
      packages=['hitcpy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=findRequirements(),
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
