SQLALchemy_demo
===============

a SQLAlchemy demo for postgreSQL

### SQLAlchemy_demo uses:

+ [Python-2.7.5+](https://www.python.org/download/releases/2.7.5 "Python") 
+ [SQLAlchemy v0.9.4 ](http://docs.sqlalchemy.org/en/rel_0_9/ "SQLAlchemy")
+ [postgresql-9.3](http://www.postgresql.org/download/linux/debian/ "postgres")
+ [alembic](http://alembic.readthedocs.org/en/latest/ "alembic")
+ More to come.... (See TODO.md)


1. Setup instructions - python pip and a virtual environment:
---------------
  1. Get pyhton pip (http://pip.readthedocs.org/en/latest/installing.html)
  1. Get virtualenv via pip `$ pip install virtualenv`
  1. Make a virtual env directory `$ mkdir virt_env`
  1. Make sqla_demo's venv `$ virtualenv virt_env/sqla_demo_venv`
  1. Activate the venv `$ source virt_env/sqla_demo_venv/bin/activate` 

2. Setup instructions - setup demo
-------------
  1. `$ git clone https://github.com/jlgoldb2/SQLALchemy_demo.git`
  1. `$ cd SQLAlchemy_demo`
  1. `$ pip install -r stable-reqs.txt`




3. Setup instructions - postgresql:
---------------
  1. Install postgresql (>=9.1.13) e.g. `$ sudo apt-get install postgresql`
  1. sudo open pg_hba.conf `$ sudo gedit /etc/postgresql/9.1/main/pg_hba.conf`
  1. Scroll down. Set up the postgresql config to trust localhost:

        > # Database administrative login by Unix domain socket
        > local   all     postgres                         trust
        and....

        > # "local" is for Unix domain socket connections only
        > local   all     all                             trust

    

        
  

4. Start the demo: postgres db setup
---------------
  1  `$ sudo adduser postgres`  <-- may already exist. it's okay. proceed.
  1 give postgres a password `$ sudo passwd postgres`
  1. follow the prompts; enter the same password twice.
  1. check to see in server is started `$ service postgresql status`
  1. starts the postgres server`$ sudo service postgresql start` 
  1. `$ sudo su postgres` changes user to postgres for postgresql connection
  1. `$ psql` starts the postgresql shell

  1. lists databases on the pSQL server.  `postgres=# \l` 

        (the `postgres=#` means you are currently on the postgres db inside psql)
        
        You should see 3 databases: postgres, template0, and template1. 
        
        Leave them alone. They are for advanced use/users only.
  1. 



DEV
------ 
+ stable requirements frozen with `$ pip freeze > stable-reqs.txt`
+ dev requirements (less stable)  `$ pip freeze > dev-reqs.txt`
+ instruction sets:
-------
  + http://www.thegeekstuff.com/2009/04/linux-postgresql-install-and-configure-from-source/