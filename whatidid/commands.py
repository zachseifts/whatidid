
import json
import hashlib

from sys import exit
from os import path, makedirs
from getpass import getuser
from datetime import datetime
from time import time
from ConfigParser import ConfigParser, RawConfigParser, NoSectionError

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


class InitCommand(Command):
    ''' Implements a command for setting everything up.
    '''

    def __init__(self, **kwargs):
        super(InitCommand, self).__init__(**kwargs)

    def run(self):
        configrc = '%s/.widrc' % (path.expanduser('~'))
        if not path.exists(configrc):
            print u'There is no ~/.widrc file, createing one.'
            config = RawConfigParser()
            config.add_section('storage')
            config.set('storage', 'path', path.expanduser('~'))
            config.add_section('formats')
            config.set('formats', 'update-show-format', '%A')
            with open(configrc, 'wb') as configfile:
                config.write(configfile)


class UpdateCommand(BaseUpdateCommand):
    ''' Implements a class for the update command.
    '''

    def __init__(self, **kwargs):
        self.message = kwargs.get('message', None)
        self.tags = kwargs.get('tags', [])
        super(UpdateCommand, self).__init__(**kwargs)

    def run(self):
        data_path = self.get_data_path(self.type)

        try:
            with open(data_path, 'rb') as fp:
                existing_data = json.load(fp)
        except ValueError:
            existing_data = []

        if self.message:
            m = hashlib.md5()
            created = int(time())
            m.update(str(created) + self.message)
            existing_data.append({
                'id': m.hexdigest(),
                'created': created,
                'tags': self.tags,
                'message': self.message}
            )
            with open(data_path, 'wb') as fp:
                data = json.dump(existing_data, fp, sort_keys=True, indent=4)
        else:
            print u'No message specified'
            exit(1)


class UpdateShowCommand(BaseUpdateCommand):
    ''' Implements a class for the update-show command.
    '''

    def __init__(self, **kwargs):
        year, current_week, weekday = datetime.now().isocalendar()
        week = kwargs.get('week', None)
        if week is None:
            week = current_week
        self.week = int(week)
        super(UpdateShowCommand, self).__init__(**kwargs)

    def run(self):
        data_path = self.get_data_path(self.type, self.week)
        try:
            with open(data_path, 'rb') as fp:
                existing_data = json.load(fp)
                for update in existing_data:
                    out = u'%s' % (datetime.fromtimestamp(int(update['created'])).strftime(self.update_show_format))
                    if update['tags']:
                        print u'%s: %s: %s' % (out, ','.join(update['tags']), update['message'])
                    else:
                        print u'%s: %s' % (out, update['message'])
        except ValueError:
            print u'There are no messages.'


class TodoCommand(Command):
    ''' Implements a class for the todo command.
    '''

    def __init__(self, **kwargs):
        self.message = kwargs.get('message', None)
        self.tags = kwargs.get('tags', [])
        super(TodoCommand, self).__init__(**kwargs)

    def run(self):
        data_path = self.get_data_path('todo')

        try:
            with open(data_path, 'rb') as fp:
                existing_data = json.load(fp)
        except ValueError:
            existing_data = []

        if self.message:
            m = hashlib.md5()
            created = int(time())
            m.update(str(created) + self.message)
            existing_data.append({
                'id': m.hexdigest(),
                'created': created,
                'tags': self.tags,
                'message': self.message}
            )
            with open(data_path, 'wb') as fp:
                data = json.dump(existing_data, fp, sort_keys=True, indent=4)
        else:
            print u'No todo item specified'
            exit(1)

