SQLALchemy_demo
===============

a SQLAlchemy demo for postgreSQL and alembic

### SQLAlchemy_demo uses:

+ [Python-2.7.5+](https://www.python.org/download/releases/2.7.5 "Python") 
+ [SQLAlchemy v0.9.4 ](http://docs.sqlalchemy.org/en/rel_0_9/ "SQLAlchemy")
+ [postgresql-9.3](http://www.postgresql.org/download/linux/debian/ "postgres")
+ [alembic](http://alembic.readthedocs.org/en/latest/ "alembic")
+ More to come.... (See TODO.md)


1. setup instructions - python pip and a virtual environment:
---------------
  1. Get [python pip](http://pip.readthedocs.org/en/latest/installing.html "pip") `sudo apt-get install python-pip`
  1. Get virtualenv via pip `pip install virtualenv`
  1. Make a virtual env directory `mkdir virt_env`
  1. Make sqla_demo's venv `virtualenv virt_env/sqla_demo_venv`
  1. Activate the venv `source virt_env/sqla_demo_venv/bin/activate` 

2. setup instructions - setup demo
-------------
  1. `git clone https://github.com/jlgoldb2/SQLALchemy_demo.git`
  1. `cd SQLAlchemy_demo`
  1. `pip install -r stable-reqs.txt`




3. setup instructions - postgresql:
---------------
  1. Install postgresql (>=9.1.13) e.g. `sudo apt-get install postgresql`
  1. sudo open pg_hba.conf `sudo gedit /etc/postgresql/9.1/main/pg_hba.conf`
  1. Scroll down. Set up the ph_hba.conf to trust localhost:

        # Database administrative login by Unix domain socket
        local   all     postgres                         trust
        
        # "local" is for Unix domain socket connections only
        local   all     all                             trust

    

        
  

4. postgres and psql
---------------

  1. `$ sudo su postgres`
  2. `$psql`
 
=======
  1.  add user postgres `sudo adduser postgres`  <-- may already exist. it's okay. proceed.
  1. give postgres a password `sudo passwd postgres`
  1. follow the prompts; enter the same password twice.
  1. check to see in server is started `service postgresql status`
  1. starts the postgres server`sudo service postgresql start` 
  1. change user to postgres for postgresql connection `sudo su postgres`
  1. start the postgresql shell `psql`
  1. lists databases on the pSQL server postgres=# `\l`

    + the `postgres=#` means you are currently on the postgres db inside psql
    + You should see 3 databases: postgres, template0, and template1. Leave them alone. They are for advanced use/users only.
  
  1. press 'q' to exit that view
  1. list users postgres=# `\du`


5. create a user and a db
-----------

  1. create a user: postgres=# `CREATE USER jasonlouis;`
      + you should see a `CREATE ROLE` message to confirm success
      + notice the `;` at the end of the command. it executes the SQL code.
  1. add a password (`password`) to the user `jasonlouis`: postgres=# `ALTER ROLE jasonlouis WITH PASSWORD 'password';`
      + you should see a `ALTER ROLE` message to confirm success
  1. create `testdb` owned by our user `jasonlouis`: postgres=# `CREATE DATABASE testdb WITH OWNER jasonlouis;`
      + should see a `CREATE DATABASE` if it worked.

6. run the tests:
----------
  1. run the tests.
  1. interpret.
  1. move on.

7. run the app: 
------------
  1. Run the app.
  1. go through the config prompts.
  1. Look at the tables of the active database.
  1. Look at the tables in python

8. change the tables:
------------
  1. `git checkout table-change`
  1. oh no!! the tables are different. 
  1. we gotta change our tables.
  1. move on.

9. demo alembic
------
  * alembic has: 
    + schema
    + create_migration
    + migrate
    + rollback

  1. look at schema
  1. look at create_migration
  1. look at files.
  1. migrate.
  1. look at files again. see diffs.
  1. rollback.
  1. look at files. looks like orig.


DEV
------ 
+ stable requirements frozen with `pip freeze > stable-reqs.txt`
+ dev requirements (less stable)  `pip freeze > dev-reqs.txt`
+ instruction sets:
-------
  + [intall postgreSQL in 9 steps](http://www.thegeekstuff.com/2009/04/linux-postgresql-install-and-configure-from-source/ "postgresql install")
