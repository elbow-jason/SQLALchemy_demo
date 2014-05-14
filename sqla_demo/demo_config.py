#machine_config['py
#demo_helpers.py
import os.path
import json
import unicodedata as ucd

#my_db = 'postgresql://jasonlouis:password@localhost:5432/test'

#globals in python are restricted to the module's (read: this file's) 
    #scope. So, there is no need to worry about the 'globals' 
    #polluting the namespace.

conn_config = {}
config_declared = False

#a couple of templates for printing in a table
header_spacer = '%10s %15s %13s'
column_spacer = '%10s %15s %10s'

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
    choice = False
    while choice != 'Y' and choice != 'y' and choice != 'N' and choice != 'n':
        choice = raw_input('Reconfigure connection? (y or n): ')
        if choice == 'y' or choice == 'Y':
            get_URI_info()
        elif choice != 'n' and choice != 'N':
            print 'Invalid choice. Please try again.'

def erase_config():
    global conn_config
    conn_config['DB_URI']   = ''
    conn_config['DB_TYPE']  = ''
    conn_config['USERNAME'] = ''
    conn_config['PASSWORD'] = ''
    conn_config['DOMAIN']   = ''
    conn_config['PORT']     = ''
    conn_config['DB_NAME']  = ''


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
    is_a_file = os.path.isfile('config.json')
    if is_a_file:
        print 'config.json found!'
        return True
    else: 
        print 'config.json not found.'
        return False

def load():
    global conn_config
    print "loading config file..."
    filer   = open('config.json')
    holder  = filer.read()
    holder = json.loads(holder)

    for key in holder.keys():
        value       = str(holder[str(key)])
        new_key     = str(key)
        del holder[key]
        holder[new_key] = value
        print new_key, "  is  " ,holder[new_key]
        conn_config[new_key] = holder[new_key]

def print_config():
    global conn_config
    for i in conn_config.keys():
        print i, 'is', conn_config[i]

def save():
    global conn_config
    json_config = json.dumps(conn_config)
    print json_config
    json_config = str(json_config)
    filer = open('config.json', 'w')
    filer.write(json_config)
    filer.close()


def setup():
    checker = check()
    if checker:
        declare()
        print_config()
        load()
        print_config()
    else:
        declare()
        get_URI_info()
        print_config()
        save()
        print "file saved?:", checker()
