import transaction
from wowf.lib.auth import Auth
from wowf.scripts import BaseCommand, make_main


class SendInviteCommand(BaseCommand):

    def run(self):
        transaction.begin()
        emails = []
        while True:
            email = raw_input('Email: ')
            emails.append(email)
            again = raw_input('Add another email ([y]/n)? ')
            if again.upper() == 'N':
                break
        Auth.send_invite(emails)
        transaction.commit()


main = make_main(SendInviteCommand)