.. whatidid documentation master file, created by
   sphinx-quickstart on Mon Nov 19 09:40:13 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

What I did (whatidid) documentation
===================================

A minimalist command line app that helps you keep track of what you did this week.

Install
=======

You can install whatidid with pip, by downloading the package and installing
from the setup.py, or you can build it yourself.

You need to have a Mac and Dropbox installed to use this.

Usage
=====

This is how you use whatidid

Updating your status
--------------------

::

    $ wid update -m "This is the content of my update"
    $

Showing your updates
--------------------

::

    $ wid update-show
    Monday: This is a different update
    Monday: This is the content of my update

Mailing your updates to someone else
------------------------------------

::

    $ wid-update-mail user@example.com
    $

Modules
=======

.. automodule:: whatidid
   :members:

.. automodule:: whatidid.commands
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

