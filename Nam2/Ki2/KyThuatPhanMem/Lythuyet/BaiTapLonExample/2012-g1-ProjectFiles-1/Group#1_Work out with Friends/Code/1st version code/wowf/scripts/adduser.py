import transaction
from getpass import getpass
from wowf.lib.auth import Auth
from wowf.models import User
from wowf.scripts import BaseCommand, make_main


class AddUserCommand(BaseCommand):

    def run(self):
        transaction.begin()
        while True:
            username = raw_input('Username: ')
            email = raw_input('Email: ')
            while True:
                gender = raw_input('Gender (M/F): ')
                if gender not in ('M', 'F'):
                    print 'Gender must be M or F!'
                else:
                    break
            while True:
                password1 = getpass('Password: ')
                password2 = getpass('Repeat password: ')
                if password1 != password2:
                    print "Passwords don't match!"
                else:
                    break
            user = User.create(username, email, password1, gender, dob, weight, height)
            Auth.register(user, login=False)
            again = raw_input('Add another user ([y]/n)? ')
            if again.upper() == 'N':
                break
        transaction.commit()


main = make_main(AddUserCommand)