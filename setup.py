from setuptools import setup

setup(name='whatidid',
      version='1.6.3',
      description='A minimalist command line app for life logging.',
      long_description='An application that helps you log your life, see the github page for more info.',
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

