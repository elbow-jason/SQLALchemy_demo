#machine_config['py
#demo_helpers.py
import os.path
import json
import unicodedata as ucd

#my_db = 'postgresql://jasonlouis:password@localhost:5432/test'

#globals in python are restricted to the module's (read: this file's) 
    #scope. So, there is no need to worry about the 'globals' 
    #polluting the namespace.

config_file = 'config.json'

conn_config = {}
config_declared = False

#a couple of templates for printing in a table
header_spacer           = '%10s %15s %13s'
column_spacer           = '%10s %15s %10s'


#define a class for configuration
def declare():
    global config_declared
    if not config_declared:
        erase_config()
        config_declared = True
        print 'connection config declared...'
    else: 
        print 'connection config already declared...'
        reconfigure()

def reconfigure():
    choice = are_you_sure()
    if choice:
        get_URI_info()
        return True
    else:
        return False

def erase_config():
    global conn_config
    for key in conn_config.keys():
        conn_config[key] = ''
    """
    conn_config['DB_URI']   = ''
    conn_config['DB_TYPE']  = ''
    conn_config['USERNAME'] = ''
    conn_config['PASSWORD'] = ''
    conn_config['DOMAIN']   = ''
    conn_config['PORT']     = ''
    conn_config['DB_NAME']  = ''
"""

def change_one(key):
    conn_config[key] = raw_input(key + ' new value: ')

def get_URI_info():
    #bring in globals
    global conn_config
    #assign user inputs to globals

    
    #leave prompts empty to keep defaults
    print '\n\nLeave blank to keep current value. To change enter the new value'
        #print the current DB_URI or <blank>
    print 'Current DB URI: ', conn_config['DB_URI'] or '<blank>', '\n'
    print header_spacer%('item','current','new')
    print header_spacer%('----','-------','---')
    change('DB_TYPE')
    change('USERNAME')
    change('PASSWORD')
    change('DOMAIN')
    change('PORT')
    change('DB_NAME')
    assemble_URI()
    print "\n New DB URI: ", conn_config['DB_URI']

def change(key):
    global conn_config
    conn_config[key] = str(raw_input(column_spacer%(key, conn_config[key] or \
        '<blank>',' '))) or conn_config[key]

    #assemble
def assemble_URI():
    global conn_config
    conn_config['DB_URI'] = ''
    uri_add('DB_TYPE')
    uri_add('://')
    uri_add('USERNAME')
    uri_add(':')
    uri_add('PASSWORD')
    uri_add('@')
    uri_add('DOMAIN')
    uri_add(':')
    uri_add('PORT')
    uri_add('/')
    uri_add('DB_NAME')

def uri_add(key):
    try:
        conn_config['DB_URI'] += conn_config[key]
    except:
        conn_config['DB_URI'] += key

#checks for config['json.
# if config['json is not found, the user is prompted for the config data.
def check():
    is_a_file = os.path.isfile(config_file)
    if is_a_file:
        print config_file,' found!'
        return True
    else: 
        print config_file, 'NOT found.'
        return False

def load():
    global conn_config
    print "loading config file..."
    filer   = open(config_file)
    holder  = filer.read()
    holder = json.loads(holder)

    #FORCE assignment of keys rather than assigning entire json object
    for key in holder.keys():
        value       = str(holder[str(key)])
        new_key     = str(key)
        del holder[key]
        holder[new_key] = value
        conn_config[new_key] = holder[new_key]

def print_config():
    global conn_config
    print_spacer = '%10s %6s  %10s'
    for i in conn_config.keys():
        print print_spacer % (i, 'equals' ,conn_config[i])

def save():
    global conn_config
    json_config = json.dumps(conn_config)
    print json_config
    json_config = str(json_config)
    filer = open(config_file, 'w')
    filer.write(json_config)
    filer.close()

def delete_saved():

    os.remove(config_file)

def setup():
    checker = check()
    if checker:
        declare()
        load()
        print_config()
    else:
        declare()
        get_URI_info()
        print_config()
        save()
        checker = check()
        print "file saved?:", checker

def rewrite():
    rewritten = reconfigure()
    if rewritten:
        save()
        declare()
        load()
        print_config()
    return rewritten

def are_you_sure():
    choice = False
    while choice != 'Y' and choice != 'y' and choice != 'N' and choice != 'n':
        choice = raw_input('Are you sure? (y or n): ')
        if choice == 'y' or choice == 'Y':
            return True
        elif choice != 'n' and choice != 'N':
            print 'Invalid choice. Please try again.'
        else:
            return False