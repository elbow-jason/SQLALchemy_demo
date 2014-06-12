#machine_config['py
#demo_helpers.py
import os.path
import json

#my_db = 'postgresql://jasonlouis:password@localhost:5432/test'

#globals in python are restricted to the module's (read: this file's) 
    #scope. So, there is no need to worry about the 'globals' 
    #polluting the namespace.

#a couple of templates for printing in a table
config_file             = 'config.json'
conn_config             = {}
header_spacer           = '%10s %15s %13s'
column_spacer           = '%10s %15s %10s'
declared                = False

#define a class for configuration
def declare():
    global declared
    blank_config()
    print 'connection config blanked...'
    declared = True


def reconfigure():
    try:
        chosen = choice('reconfigure?')
        if chosen:
            get_URI_info()
            return True
        else:
            return False
    except KeyError as e:
        print 'KeyError for',e, 'Connection was not declared (use declared() first)'
    print 

def blank_config():
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
    print '----'
    print '\nLeave blank to keep current value.\nTo change enter the new value'
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
        return True
    else: 
        return False

def load():
    global conn_config
    print  "loading config file..."
    filer  = open(config_file)
    holder = filer.read()
    holder = json.loads(holder)

    #FORCE assignment of keys rather than assigning entire json object
    for key in holder.keys():
        value                   = str(holder[str(key)])
        new_key                 = str(key)
        del holder[key]
        holder[new_key]         = value
        conn_config[new_key]    = holder[new_key]

def print_config():
    global conn_config
    print_spacer = '%10s %1s  %10s'
    print '\n'
    print 'CURRENT CONFIG\n'
    print print_spacer % ('item','','value')
    print print_spacer % ('------','', '------')
    for i in conn_config.keys():
        print print_spacer % (i, ':' ,conn_config[i])
    print '\n'

def save():
    global conn_config
    checker = check()
    if checker:
        chosen = choice('overwrite old config file?')
    else:
        chosen = True
    if chosen:
        json_config = json.dumps(conn_config)
        json_config = str(json_config)
        filer = open(config_file, 'w')
        filer.write(json_config)
        filer.close()
        print 'file saved...'
    else: 
        print "config not saved."

def delete_config_file():
    checker = check()
    if checker:
        chosen = choice("This will delete the config file. Are you sure?")
        if chosen:
            os.remove(config_file)
            checker = check()
            print "file deleted? :", not checker
    else:
        print "config file not found. cannot delete."

def setup():
    checker = check()
    if (checker == True):
        print "config file found."
        load()
        print_config()
        chosen = choice("Change current config?")
        if chosen:
            new_config()
        else:
            print 'keeping current config...'
    else:
        print 'config file not found.'
        print 'initializing new config...'
        declare()
        new_config()
    print "configuration setup complete..."

def new_config():
    get_URI_info()
    print_config()
    chosen = choice("save config?")
    if chosen:
        save()
        checker = check()
        if (checker != True):
            raise Exception('file not saved correctly or checker is broken')

def rewrite():
    rewritten = reconfigure()
    if rewritten:
        save()
        declare()
        load()
        print_config()
    return rewritten

def choice(question):
    chosen = False
    while chosen != 'Y' and chosen != 'y' and chosen != 'N' and chosen != 'n':
        question = question + '(y or n): '
        chosen = raw_input(question)
        if chosen == 'y' or chosen == 'Y':
            return True
        elif chosen != 'n' and chosen != 'N':
            print 'Invalid choice. Please try again.'
        else:
            return False
