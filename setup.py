from setuptools import setup

setup(name='array_viewer',
      version='0.1',
      description='A simple numpy 2D array viewer',
      url='https://github.com/edelsonc/array_viewer',
      author='edelsonc',
      author_email='cje5555@bellsouth.net',
      license='MIT',
      packages=['array_viewer'],
      install_requires= [
        'matplotlib'
      ],
      zip_safe=False
)
