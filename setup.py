from setuptools import setup

with open('README.md') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(name='_42',
      version='0.1.0',
      description='Decorator that runs everything (in its way)',
      long_description=long_description,
      url='http://github.com/marcorosa/_42',
      author='Marco Rosa',
      author_email='marcor165@hotmail.it',
      license='MIT',
      packages=['_42'],
      keywords='decorator'
)