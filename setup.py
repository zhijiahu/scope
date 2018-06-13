from setuptools import setup
from setuptools import find_packages


setup(name='scope',
      version='1.0.0',
      description='A simple monitoring tool',
      author='Zhijia Hu',
      author_email='z.jia.hu@gmail.com',
      url='https://github.com/zhijiahu/scope',
      download_url='https://github.com/zhijiahu/scope/tarball/1.0.0',
      license='MIT',
      install_requires=[
          'pyaml>=17.10.0',
          'aiohttp>=2.3.1',
          'rollbar>=0.14.0',
      ],
      extras_require={
          'tests': ['pytest-asyncio',
          ],
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
packages=find_packages())
