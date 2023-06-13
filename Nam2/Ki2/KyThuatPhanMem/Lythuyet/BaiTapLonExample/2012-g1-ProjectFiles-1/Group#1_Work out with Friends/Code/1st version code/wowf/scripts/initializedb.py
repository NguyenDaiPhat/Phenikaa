from wowf.models import initialize_db
from wowf.scripts import BaseCommand, make_main


class InitializeDBCommand(BaseCommand):

    def run(self):
        initialize_db(self.env.registry.settings)


main = make_main(InitializeDBCommand)