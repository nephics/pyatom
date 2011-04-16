from setuptools import setup

project = 'pyatom'
version = 1.2

setup(name=project,
      version=version,
      description="A Python library for generating Atom 1.0 feeds.",
      long_description=open('README.rst').read(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development',
      ],
      platforms='any',
      keywords='feed rss atom',
      author='Ramana',
      author_email='sramana9@gmail.com',
      url='http://bitbucket.org/sramana/pyatom',
      license='BSD',
      py_modules=['pyatom'],
     )
