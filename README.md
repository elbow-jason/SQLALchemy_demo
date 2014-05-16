SQLALchemy_demo
===============

a SQLAlchemy demo for postgreSQL

More to come.... (See TODO.md)

SQLAlchemy_demo uses Python-2.7.5



Setup instructions (python):
---------------
  1. Get pyhton pip (http://pip.readthedocs.org/en/latest/installing.html)
  2. `$ pip install virtualenv`
  3. `$ mkdir virt_env`
  4. `$ virtualenv virt_env/sqla`

Setup instructions (postgresql):
---------------
  1. Install postgresql (>=9.1.13) e.g. `$ sudo apt-get install postgresql`
  2. Set up the postgresql config to trust localhost:
      edit /etc/postgresql/9.1/main/pg_hba.conf (sudo required)

        below    # "local" is for Unix domain socket connections only

        change  local   all     all     peer

        to      local   all     all     trust

Start the demo: postgres db setup
---------------
  1. `$ sudo service postgresql start` starts the postgres server
  1. `$ sudo su postgres` changes user to postgres for postgresql connection
  3. `$ psql` starts the postgresql shell

  4. `postgres=# \l` lists databases on the pSQL server. 
        (the `postgres=#` means you are currently on the postgres db)
        
        You should see 3 databases: postgres, template0, and template1. 
        
        Leave them alone. They are for advanced use/users only.
  5. 

