from setuptools import setup

setup(name='whatidid',
      version='1.5',
      description='Keep track of your life',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
      ],
      keywords='lifelogging whatidid',
      url='https://github.com/zachseifts/whatidid',
      author='Zach Seifts',
      author_email='zach.seifts@gmail.com',
      license='MIT',
      packages=['whatidid'],
      zip_safe=False,
      scripts=['bin/wid', 'bin/wid-update-mail'])

