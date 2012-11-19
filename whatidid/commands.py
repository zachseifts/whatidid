from sys import exit
from os import path, makedirs
from getpass import getuser
from datetime import datetime
from time import time

class DropboxNotInstalledException(Exception): pass

class Command(object):
    ''' A base class for a command.

    Subclass this class to generate a command:

        >>> from whatidid.commands import Command
        >>> class MyCommand(Command):
        >>> def run(self):
        >>>     print 'ran the command'
        >>> command = MyCommand()
        >>> command.run()
        ran the command

    Get the path of the data file and if it does not exist it will create it:

        >>> from whatidid.commands import Command
        >>> command = Command()
        >>> command.get_data_path('foo')
        /Users/user/Dropbox/.whatidid/foo/2012/34.md

    '''

    def __init__(self, **kwargs):
        pass

    def get_data_path(self, key):
        year, week, weekday = datetime.now().isocalendar()
        dropbox = '/Users/%s/Dropbox' % (getuser());
        if not path.exists(dropbox):
            raise DropboxNotInstalledException('Dropbox path does not exist.')
        wid_dir = '%s/.whatidid' % (dropbox)
        if not path.exists(wid_dir):
            makedirs(wid_dir)
        data_dir = '%s/%s/%d' % (wid_dir, key, year)
        if not path.exists(data_dir):
            mkdirs(data_dir)
        data_path = '%s/%d.md' % (data_dir, week)
        if not path.exists(data_path):
            updates = open(data_path, 'w+')
            updates.write('')
            updates.close()
        return data_path

    def get_data(self, key):
        data_path = self.get_data_path(key)
        data = open(data_path, 'rb')
        return_data = [line.rstrip() for line in data]
        data.close()
        return return_data;


    def run(self):
        raise NotImplementedError('The run() function is not implemented.')


class UpdateCommand(Command):
    ''' Implements a class for the update command.
    '''

    def __init__(self, **kwargs):
        self.message = kwargs.get('message', None)
        super(UpdateCommand, self).__init__()

    def run(self):
        data_path = self.get_data_path('updates')
        if self.message:
            f = open(data_path, 'a')
            f.write("%d:%s\n" % (int(time()), self.message))
            f.close()
        else:
            print 'No message specified'
            exit(1)

class UpdateShowCommand(Command):
    ''' Implements a class for the update-show command.
    '''

    def run(self):
        for line in self.get_data('updates'):
            timestamp, message = line.split(':');
            print "%s: %s" % (datetime.fromtimestamp(int(timestamp)).strftime('%A'), message)

