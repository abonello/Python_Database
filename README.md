# Using Python to controle a Database

## CONNECT TO A MYSQL DATABASE

This software will attempt to connect and query the MySQL server. It will need to manage the connection.

## DRIVER BASED DATABASE ACCESS

For flexibility we are going to keep our connection code and code that performs queries ‘decoupled’ from the main system.

This is a good approach because we can then add in a layer of abstraction later that will make it possible for our programs that perform database operations to be almost ‘agnostic’ of which database they are working with

The approach used is to expose each kind of database available through a ‘driver’ or a class module that knows specific methods for accessing one particular database system.

By doing so, we can then write our applications and not have to worry too much about the specifics of saving data to any particular database system. This could save us time and money!

### Setup:
<PRE>

\your project\
              |
               – database
              |          |
              |           – __init__py
              |          |
              |           – mysql.py
              |
               – main.py
              |
               – settings.py
</PRE>

To create a Python package, we simply need to create a folder with an (empty) \_\_init\__.py file and any module files we may need.

mysql.py file will contain the MySQL class driver code.

More class drivers can be added later for Postgres or Sqlite if needed.

main.py - application code

settings.py - will take care of any connection settings for our database and potentially any other settings that our application would need later.