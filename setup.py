from setuptools import find_packages
from setuptools import setup
from wifind._version import __version__

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='wifind',
      version=__version__,
      description="Wi-Fi indoor positioning system",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Dinelli Michele',
      url='https://github.com/micheledinelli/wifind',
      author_email='dinellimichele00@gmail.com',
      install_requires=[
          'pandas', 'scikit-learn', 'access_points'
      ],
      entry_points={
          'console_scripts': ['wifind = wifind.__main__:main']
      },
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Customer Service',
          'Intended Audience :: System Administrators',
          'Operating System :: Microsoft',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities'
      ],
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      platforms='any')