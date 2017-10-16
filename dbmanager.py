"""
This is a utility to check and modify the database for testing purposes, has no use for end users, just for developers
""" 

import sqlite3
import models as dbhelper

def create_database():
	sqlite_file = 'database.db'    # name of the sqlite database file
	table_name = 'users'	# name of the table to be created
	id_column='id_column'

	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	# Creating a new SQLite table 
	c.execute('CREATE TABLE {tn} ({nf} {ft})'\
			.format(tn=table_name, nf=id_column, ft='INTEGER PRIMARY KEY AUTOINCREMENT'))

	#add next column
	new_column='username'
	column_type='TEXT'
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
			.format(tn=table_name, cn=new_column, ct=column_type))

	#add next column
	new_column='password'
	column_type='TEXT'
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
			.format(tn=table_name, cn=new_column, ct=column_type))
	

	conn.execute('''CREATE TABLE UserSaves
	                        (
	                        id_column INTEGER,
	                        KeyWord Text,
	                        TimeStamp DATE,                        

	                        FOREIGN KEY(id_column) REFERENCES users(id_column)
	                        );''')
	print("Database and table created")
	# Committing changes and closing the connection to the database file
	conn.commit()

#prints all user data in users table
def show_entries():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute("SELECT * FROM users")
	print(c.fetchall())
def deleateSearches():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute("SELECT * FROM users")
	print(c.fetchall())

running=True
print("Database Manager running. Type \n show: to see the database, \n create: to recreate the database, \n exists: to see if a user exists, \n delete: to delete a user, \n password: to get the password of a user, \n insert: to insert new user  \n showsearches: to show a user's search history \n exit:  to stop the manager.")
while(running==True):
	cmd=input("Enter command: ")
	if cmd == "show":
		show_entries()
	elif cmd == "exists":
		n=input("Enter username to query if exists: ")
		dbhelper.userExists(n)
	elif cmd == "create":
		create_database()
		
	elif cmd == "password":
		n=input("Enter username to get password for: ")
		p= dbhelper.getPassword(n)
		print(p)
		
	elif cmd=="insert":
		n=input("Enter username of user to insert: ")
		p=input("Enter password of user to insert: ")
		dbhelper.insertUser(n,p)
		print("User "+n+" with password: "+p+" inserted")
	
	elif cmd == "exit":
		print("Exiting...")
		running=False
		break
	elif cmd == "delete":
		n=input("Enter username to delete user: ")
		dbhelper.deleteUser(n)
	elif cmd == "showsearches":
		n=input("Enter username of user to get search history for: ")
		dbhelper.showSearches(n)
	elif cmd =="getId":
		n=input("Enter username to get ID for: ")
		print(dbhelper.getId(n))
	else:
		print("Command not recognized")