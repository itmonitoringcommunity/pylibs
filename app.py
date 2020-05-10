import os
import sys
import cmd
import getpass
from src import *

APIURL = 'http://127.0.0.1:8000/'
USERNAME = 'admin'
PASSWORD = 'admin'

api = CustomApi(APIURL)
api.login(USERNAME, PASSWORD)

menu = CustomMenu()
service1 = CustomScheduled(api)
service2 = CustomScheduledCron()


class MyShell(cmd.Cmd, object):
    intro = 'Welcome to the service shell.   Type help or ? to list commands.\n'
    prompt = '[Shell Prompt] :'

    # ----- basic commands -----
    def do_help(self, line):
        for item in menu.get_help_text():
            print(item)

    def do_login(self, line):
        print(line)
        username = input('Please enter username: ')
        password = getpass.getpass(prompt='Please enter password: ')

        api.login(username, password)
        print(api.msg)

    def do_logout(self, line):
        api.logout()
        print(api.msg)

    def do_start(self, line):
        if (api.token is ''):
            print('Please login before service started')
        else:
            service1.start()
            # service2.start()
            print('Scheduler Service started')

    def do_restart(self, line):
        if (api.token is ''):
            print('Please login before service restarted')
        else:
            service1.restart()
            # service2.restart()
            print('Schedular Service restarted')

    def do_stop(self, line):
        if (api.token is ''):
            print('Please login before service stopped')
        else:
            service1.stop()
            # service2.stop()
            print('Schedular Service stopped')

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_clear(self, line):
        os.system('cls')  # on windows
        # os.system('clear')  # on linux / os x

    def do_exit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def cmdloop(self, intro=None):
        print(self.intro)
        while True:
            try:
                super(MyShell, self).cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("^C")


# ----- out of class -----

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(str, arg.split()))


if __name__ == '__main__':
    app = MyShell()
    app.cmdloop()
