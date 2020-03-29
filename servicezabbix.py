"""
Shows a list of all current issues (AKA tripped triggers)
"""

from pyzabbix import ZabbixAPI
from datetime import datetime
import time

# The hostname at which the Zabbix web interface is available

def get_hosts(zabbix_server = 'https://zabbix.example.com',api_username='Admin',api_password='zabbix'):
    zapi = ZabbixAPI(zabbix_server)
    zapi.login(api_username, api_password)
    
    hosts = zapi.host.get(output='extend')
    print(hosts)
    return hosts 

def get_host_groups(zabbix_server = 'https://zabbix.example.com',api_username='Admin',api_password='zabbix'):
    zapi = ZabbixAPI(zabbix_server)
    zapi.login(api_username, api_password)
    
    hostgroups = zapi.hostgroup.get(output='extend')
    print(hostgroups)
    return hostgroups

def get_triggers(zabbix_server = 'https://zabbix.example.com',api_username='Admin',api_password='zabbix'):        
    zapi = ZabbixAPI(zabbix_server)
    
    # Login to the Zabbix API
    zapi.login(api_username, api_password)
    
    # Get a list of all issues (AKA tripped triggers)
    triggers = zapi.trigger.get(output = 'extend',
                                selectHosts = 'extend',
                                expandData = 1,
                                expandDescription = 1,
                                skipDependent = 1,
                                withLastEventUnacknowledged = 1,
                                min_severity = 1,
                                filter = 
                                {
                                    value : 1,
                                    status : 0
                                },
                                sortfield = 'lastchange',
                                sortorder = 'DESC'
                                )
    
    # Do another query to find out which issues are Unacknowledged
#    unack_triggers = zapi.trigger.get(only_true=1,
#                                      skipDependent=1,
#                                      monitored=1,
#                                      active=1,
#                                      output='extend',
#                                      expandDescription=1,
#                                      selectHosts=['host'],
#                                      withLastEventUnacknowledged=1,
#                                      )
#    unack_trigger_ids = [t['triggerid'] for t in unack_triggers]
#    for t in triggers:
#        t['unacknowledged'] = True if t['triggerid'] in unack_trigger_ids \
#            else False
#    
#    # Print a list containing only "tripped" triggers
#    for t in triggers:
#        if int(t['value']) == 1:
#            print("{0} - {1} {2}".format(t['hosts'][0]['host'],
#                                         t['description'],
#                                         '(Unack)' if t['unacknowledged'] else '')
#    )
    print(triggers)
    return triggers

def get_items(zabbix_server = 'https://zabbix.example.com',api_username='Admin',api_password='zabbix',host,key):
    zapi = ZabbixAPI(zabbix_server)
    zapi.login(api_username, api_password)
    
    items = zapi.item.get(output = "extend",
                          filter={'host':host},
                          search ={'key_':key}
                          )
    
    print(items)
    return items

def get_history(zabbix_server = 'https://zabbix.example.com',api_username='Admin',api_password='zabbix',item_id = 'item_id',lasthour=4):
    zapi = ZabbixAPI(zabbix_server)
    zapi.login(api_username, api_password)
    # Create a time range
    time_till = time.mktime(datetime.now().timetuple())
    time_from = time_till - 60 * 60 * lasthour  # 4 hours
    
    # Query item's history (integer) data
    history = zapi.history.get(itemids=[item_id],
                               time_from=time_from,
                               time_till=time_till,
                               output='extend',
                               limit='5000',
                               )
    
    # If nothing was found, try getting it from history (float) data
    if not len(history):
        history = zapi.history.get(itemids=[item_id],
                                   time_from=time_from,
                                   time_till=time_till,
                                   output='extend',
                                   limit='5000',
                                   history=0,
                                   )
    
    # Print out each datapoint
#    for point in history:
#        print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
#    .strftime("%x %X"), point['value']))
    print(history)
    return history

def get_item_average(zabbix_server = 'https://zabbix.example.com',api_username='Admin',api_password='zabbix',item_id, minutes):
    zapi = ZabbixAPI(zabbix_server)
    zapi.login(api_username, api_password)
    
    time_till = time.mktime(datetime.now().timetuple())
    time_from = time_till - 60 * minutes
 
    history =  zapi.history.get(itemids=[item_id],
        time_from=time_from,
        time_till=time_till,
        output='extend',
        limit='500',
    )
    values = []
    for point in history:
        values.append(int(point['value']))
    return sum(values) / float(len(values))
