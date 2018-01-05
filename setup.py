from setuptools import setup

setup(name='DSST Locations',
      version='0.1',
      description='Downloads and parses DSST (Dantes) testing centers',
      url='https://github.com/leogodin217/dsst_locations',
      author='Leo Godin',
      author_email='leogodin217@gmail.com',
      license='MIT',
      packages=['dsst_locations'],
      zip_safe=False,
      install_requires=[
          'beautifulsoup4',
          'sure',
          'jupyter',
          'requests',
          'pandas',
          'boto3',
          'pytest',
          'pytest-watch' 
      ])