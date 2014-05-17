SQLALchemy_demo
===============

a SQLAlchemy demo for postgreSQL

SQLAlchemy_demo uses 
+ Python-2.7.5
+ SQLAlchemy 

More to come.... (See TODO.md)


Setup instructions (python and a virtual environment):
---------------
  1. Get pyhton pip (http://pip.readthedocs.org/en/latest/installing.html)
  1. Get virtualenv via pip `$ pip install virtualenv`
  1. Make a virtual env directory `$ mkdir virt_env`
  1. Make sqla_demo's venv `$ virtualenv virt_env/sqla_demo_venv`
  1. Activate the venv `$ source virt_env/sqla_demo_venv/bin/activate` 


Setup instructions (postgresql ):
---------------
  1. Install postgresql (>=9.1.13) e.g. `$ sudo apt-get install postgresql`
  2. Set up the postgresql config to trust localhost:
      edit /etc/postgresql/9.1/main/pg_hba.conf (sudo required)

        + below:     # "local" is for Unix domain socket connections only
        
          change    local   all     all     peer
          
          to        local   all     all     trust

Start the demo: postgres db setup
---------------
  1. `$ sudo service postgresql start` starts the postgres server
  1. `$ sudo su postgres` changes user to postgres for postgresql connection
  3. `$ psql` starts the postgresql shell

  4. lists databases on the pSQL server.  `postgres=# \l` 

        (the `postgres=#` means you are currently on the postgres db inside psql)
        
        You should see 3 databases: postgres, template0, and template1. 
        
        Leave them alone. They are for advanced use/users only.
  5. 

