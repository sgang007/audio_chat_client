from setuptools import setup, find_packages
# from distutils.core import setup
# import py2exe
# import sys
import os
del os.link

# sys.setrecursionlimit(5000)

with open('requirements.txt') as f:
    required = f.read().splitlines()


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='varta-chat',
      version='1.0',
      description='Audio Chat framework',
      long_description=readme(),
      url='https://github.com/sgang007/audio_chat_client',
      author='Shubhojyoti Ganguly',
      author_email='shubho.important@gmail.com',
      license='MIT',
      packages=find_packages(),
      
      install_requires=required,
		entry_points={
          'console_scripts': [
              'varta = client.__main__:key_listener',
          ]
      },
      include_package_data=True,
      zip_safe=True)
