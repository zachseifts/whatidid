A minimalist command line app for life logging.

## Requirements

 - Python 2.7
 - OSX or Linux
 - Basic knowledge of how to use the command line

## Installing

You can install wid with either pip or easy_install, I like pip:

    $ pip install whatidid

## Getting started

You will need to initialize the `~/.widrc` file and get your database structure setup before you can use the application.

   $ wid init

## Commands

You can update your updates by using `wid update` command:

    $ wid update -m "This is my status" -t tag1,tag2,tag3

You can list all of your updates by using the `wid update-show` command:

    $ wid update-show
    Monday: This is my status
    Tuesday: Did something

You can email someone by the `wid-update-mail` command:

    $ wid-update-mail user@example.com

Note: This will be moved into the `wid` command soonish.

## Advanced configuration

All of the configuration options live in the `~/.widrc` file, you can edit those values to configure your instance of wid.

### The [storage] category

#### path

Defines where the data is stored, this can be any location on the disk your user can write to.

Example:

    path = /Users/foo/Dropbox/.whatidid

### The [formats] category

#### update-show-format

Defines how the date should be formated from the results of `wid updates-show`.

Example:

    update-show-format = %m/%d/%Y

    $ wid update-show
    11/18/2012: Did something
    11/19/2012: Did something else

