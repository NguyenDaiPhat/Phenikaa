import argparse
import sys
from wowf.config import settings
from wowf.lib.utils import Storage
from pyramid.paster import bootstrap, setup_logging


def make_main(Command):
    def main(argv=None):
        if argv is None:
            argv = sys.argv
        command = Command(argv)
        sys.exit(command.run())
    return main


class BaseCommand(object):

    parser = argparse.ArgumentParser()
    parser.add_argument('config_uri', action='store', help='Configuration file to use')

    def __init__(self, argv):
        '''
        Setup the necessary environment to run the script.
        '''
        self.args = self.parser.parse_args(argv[1:])
        setup_logging(self.args.config_uri)
        try:
            self.env = Storage(bootstrap(self.args.config_uri))
        except Exception as e:
            self.env = None
            raise SystemExit(e)
        self.env.request.host = settings.host
        self.settings = settings

    def __del__(self):
        if self.env is not None:
            self.env.closer()

    def run(self):
        raise NotImplementedError()