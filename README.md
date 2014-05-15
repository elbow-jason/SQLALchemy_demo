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
        below    `# "local" is for Unix domain socket connections only`

        change  `local   all     all     peer`  <-- could be md5 vice peer

        to      `local   all     all     trust`

Start the demo:
---------------
  1. `$ sudo su postgres`
  2. `$psql`

