Requirements

This repo show my purposed solution for the ECS user case presented as part of the selection process for the role described
at https://ecs.csod.com/ux/ats/careersite/5/home/requisition/142?c=ecs

Development stages:

    * Requirements analysis.
    * Planning
    * Research
    * Development
    * Implementation

Environment set up:

A cloud development environment is available in aws.cloud9 login instructions will be sent in a separate email. Furthermore, set up 
summary is described below:

* Ubuntu 18.04 LTS hosts the MySQL 5.7 DB server
* Install python 2.7. 
* Install python devel tools.
* Install python-mysqld ($ sudo apt-get install python-mysqldb).
8 Pip install sqlalchemy.


THE SCRIPT:

    * Language: python2.7.
    * The final script will be executed as a program with the following command line arguments: 
    
        1.-  your-script.your-lang
        2.- directory-with-sql-scripts
        3.- username-for-the-db
        4.- db-host
        5.- db-name
        6.- db-password

SET UP:

    - Data Base Management system: MySQL 5.7
    - A DB needs to be upgraded regularly.
    - SQL scripts for upgrading the system are available at local hosted path location. 
    - SQL scripts are just sequential SQL statements. 
    - The DB version is stored in the same DB to be updated in a table called ‘versionTable’. This table contains a single row. A column called ‘version’ is used to store these values.
    
HOW THE DB IS UPDATED:

    - A comparison between the version stored in the DB and the number of the files contained in the above mentions path location is made to decide if the system needs updating.
    - If the version number from the DB matches the highest number from the scripts, then nothing is executed.
    - All script files higher than DB version are executed in order. 
    - There may be gaps in the filename numbering and not always there is a dot after the initial number
        045.createtable.sql
        055doSomething.sql
        056doSomethingelse.sql
        111.andDoThisAsWell.sql
    - After one file script is executed the DB version value in ‘versionTable’.

DELIVERABLE:

    - Propose a script to automate the scenario described previously. Languages accepted: Bash, Python2.7, PHP, Shell, Ruby, Powershell.

::
Running Script
    $ ./upgradeDB.py $directory-with-sql-scripts $username-for-the-db $db-host $db-name $db-password
::
::
Running Tests

Tests can be run by executing run_test.py python file found at /home/ubuntu/ECS_user_case/ECS_EXERCISE or in the src folder
if the project is clone from https://github.com/manrodri/ECS_EXERCISE.git

    $ python run_tests.py test_utils.py tests

This will run all tests contained in tests/test_utils.py folder.
