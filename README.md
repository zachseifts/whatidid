A minimalist command line app for life logging.

## Requirements

 - Python 2.7
 - OSX or Linux
 - Basic knowledge of how to use the command line

## Installing

You can install wid with either pip or easy_install, I like pip:

    $ pip install whatidid

or:

    $ pip install whatidid --upgrade

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

You can list all of your updates from a specific week by using the `-w` flag:

    $ wid update-show -w 46
    Monday: I did this
    Tuesday: tag1,tag2: This is what I did today
    Tuesday: tag1: I did something else

You can email someone by the `wid-update-mail` command:

    $ wid-update-mail user@example.com

__Note:__ This will be moved into the `wid` command soonish.

You can item your todo by using `wid todo` command:

    $ wid todo -m "This is what I need to do"

You can list all of your todos by using the `wid todo-show` command:

    $ wid todo-show
    d7d30320a8663cc5c41fbf510fe2cd72: something i need to do
    b39b4ffa530441de3b09c362942742ab: something else i need to do

You can view a todo item by using the `wid todo-show -i` command:

    $ wid todo-show -i b39b4ffa530441de3b09c362942742ab
    something else i need to do

## Configuration

All of the configuration options live in the `~/.widrc` file.

### [storage]

#### path

Defines where the data is stored, this can be any location on the disk your user can write to.

Example:

    path = /Users/foo/Dropbox/.whatidid

### [formats]

#### update-show-format

Defines how the date should be formated from the results of `wid updates-show`.

Example:

    update-show-format = %m/%d/%Y

On the command line:

    $ wid update-show
    11/18/2012: Did something
    11/19/2012: Did something else

