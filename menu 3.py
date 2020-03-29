# -*- coding: utf-8 -*-

def get_header():
    return 'Service Monitoring Center Console\n'

def get_help():
    menu ='Help Menu\n'.join([ 'login\t\tlogin the system',
             'logout\t\tlogout the system'])
    return menu