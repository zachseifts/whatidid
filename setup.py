from setuptools import setup

setup(name='whatidid',
      version='1.0',
      description='Keep track of your life',
      url='https://github.com/zachseifts/whatidid',
      author='Zach Seifts',
      author_email='zach.seifts@gmail.com',
      license='MIT',
      packages=['whatidid'],
      zip_safe=False,
      scripts=['bin/wid', 'bin/wid-update-mail'])

