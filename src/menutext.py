# -*- coding: utf-8 -*-
import json

def get_help():
    menu = []

    menu.append('---------------------------------------------------------\n')
    
    menu.append("*** Service Shell Help Menu ***\n")

    menu.append('exit \t\t close the system')
    menu.append('login \t\t login the system')
    menu.append('logout \t\t logout the system')
    menu.append('start \t\t start the scheduled service')
    menu.append('stop \t\t stop the scheduled service')
    menu.append('restart \t restart the scheduled service')

    menu.append('\n---------------------------------------------------------')

    return menu