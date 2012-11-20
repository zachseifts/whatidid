from setuptools import setup

setup(name='whatidid',
      version='1.5.7',
      description='A minimalist command line app that helps you keep track of what you did.',
      long_description='A minimalist command line app that helps you keep track of what you did last week.',
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

