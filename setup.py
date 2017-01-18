from setuptools import setup

setup(name='pyctarr',
      version='0.1',
      description='A simple numpy 2D array viewer',
      url='https://github.com/edelsonc/pyctarr',
      author='edelsonc',
      author_email='cje5555@bellsouth.net',
      license='MIT',
      packages=['pyctarr'],
      install_requires= [
        'matplotlib'
      ],
      zip_safe=False
)
