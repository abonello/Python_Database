import MySQLdb as _mysql

# Connection details for 'mydb' database
db = _mysql.connect(
    db = 'mydb',
    host = 'localhost',
    user = 'root',
    passwd = 'aWsd6y,pP')

# Initialize a cursor object to open
# the database connection
cursor = db.cursor()

# execute the SQL query
cursor.execute("SELECT * FROM people")

# Fetch all the results from the executed query
results = cursor.fetchall()
 
# close
cursor.close()
 
