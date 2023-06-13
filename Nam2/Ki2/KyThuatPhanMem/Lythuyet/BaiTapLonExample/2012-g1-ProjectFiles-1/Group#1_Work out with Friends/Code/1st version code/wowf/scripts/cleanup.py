import transaction
from wowf.lib.utils import get_subclasses
from wowf.models import tokens
from wowf.scripts import BaseCommand, make_main


class CleanupCommand(BaseCommand):

    def run(self):
        transaction.begin()
        self.delete_expired_tokens()
        transaction.commit()

    def delete_expired_tokens(self):
        for cls in get_subclasses(tokens, tokens.Token):
            cls.delete_expired()


main = make_main(CleanupCommand)