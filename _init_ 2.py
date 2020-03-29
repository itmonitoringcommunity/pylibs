import cmd,menu,authentication
import getpass

class main(cmd.Cmd):
    """Simple command processor example."""

    prompt = 'prompt: '
    intro = "Simple command processor example."

    
    def do_help(self, line):
        print(menu.get_header())
        print(menu.get_help())
    
    def do_login(self,line):
        print(line)
        username = input('Please enter username: ')
        password = getpass.getpass(prompt='Please enter password: ')
        
        if authentication.login(username,password) == True:
            print('Welcome..!!!')
        else:
            print('The answer entered by you is incorrect..!!!')
        
    def do_logout(self, line):
        print(line)
        print('Good Bye..!!!')
    
    def do_start(self, line):
        print(line)
        print('Scheduler Service started')
        print('Artifical Intelligence Service started')
        
    def do_restart(self, line):
        print(line)
        print('Schedular Service restarted')
        print('Artifical Intelligence Service restarted')
    
    def do_stop(self, line):
        print('Schedular Service stopped')
        print('Artifical Intelligence Service stopped')
        
    def do_reset_config(self, line):
        print(line)
        print('All System Config was reset')
    
    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_EOF(self, line):
        return True
    
    
    
    

if __name__ == '__main__':
    main().cmdloop()