import json

from os import path, makedirs
from datetime import datetime
from ConfigParser import ConfigParser, NoSectionError

class Command(object):
    ''' A base class for creating commands to work with the whatidid project

    Subclass this class to generate a command:

        >>> from whatidid.commands import Command
        >>> class MyCommand(Command):
        >>> def __init__(self, **kwargs):
        >>>     self.thing = 'foo'
        >>>     super(MyCommand, self).__init__(**kwargs)
        >>> def run(self):
        >>>     print 'ran the command'
        >>> command = MyCommand()
        >>> command.run()
        ran the command

    '''

    def __init__(self, **kwargs):
        configrc = '%s/.widrc' % (path.expanduser('~'))
        config = ConfigParser()
        config.read(configrc)
        try:
            storage_path = config.get('storage', 'path', path.expanduser('~'))
        except NoSectionError:
            storage_path = path.expanduser('~')
        self.storage_path = '%s/.whatidid' % (storage_path,)
        try:
            self.update_show_format = config.get('formats', 'update-show-format', '%Y')
        except NoSectionError:
            self.update_show_format = '%Y'

    def get_data_path(self, key, week=None):
        ''' Get the path of the data file for a key

        Usage:

        >>> from whatidid.commands import Command
        >>> command = Command()
        >>> command.get_data_path('foo')
        /Users/user/Dropbox/.whatidid/foo/2012/34.md

        '''
        year, current_week, weekday = datetime.now().isocalendar()
        if week is None: week = current_week
        data_dir = '%s/%s/%d' % (self.storage_path, key, year)
        if not path.exists(data_dir):
            makedirs(data_dir)
        data_path = '%s/%d.json' % (data_dir, week)
        if not path.exists(data_path):
            with open(data_path, 'wb') as updates:
                json.dump([], updates)
        return data_path

    def run(self):
        raise NotImplementedError('The run() function is not implemented.')


class BaseUpdateCommand(Command):
    ''' A base class for Update commands
    '''

    def __init__(self, **kwargs):
        self.type = 'updates'
        super(BaseUpdateCommand, self).__init__(**kwargs)


class BaseTodoCommand(Command):
    ''' A base class for Todo commands
    '''

    def __init__(self, **kwargs):
        self.type = 'todo'
        super(BaseTodoCommand, self).__init__(**kwargs)

    def get_data_path(self, key, week=None):
        ''' Overrides the default get_data_path.
        '''
        data_dir = '%s/%s' % (self.storage_path, key)
        if not path.exists(data_dir):
            makedirs(data_dir)
        data_path = '%s/items.json' % (data_dir,)
        if not path.exists(data_path):
            with open(data_path, 'wb') as updates:
                json.dump([], updates)
        return data_path

