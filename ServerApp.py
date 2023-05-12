

#  Creating Python apps using Microsoft SQL Server 2002 
#  DEVELOPER EDITION on Windows


import pyodbc as pyb
import confiles as cof

mssqlString = cof.mssqlConnectionStringDB()
conn = pyb.connect(mssqlString)
cursor = conn.cursor()
print('\n\n')


def mssqlManipulation(params):
    print(params[0])
    with cursor.execute(params[2], params[3:]) as exec:
        print("Query Executed!" if exec else "Query Failed!")
    if exec:
        print(params[1])
        conn.commit()
        print(f"{params[2].split()[0]} transaction committed.")
    else:
        conn.rollback()
        print(f"{params[2].split()[0]} transaction rolled.")
        return
    cnt = exec.rowcount
    print(f'Row affected: {str(cnt)}\n')


# Begin transaction
cursor.execute("BEGIN TRANSACTION")

# Insert New Query
tsql = ['Inserting a new row into table:', 'Successfully Inserted!',
        "INSERT INTO Employees (Name, Location) VALUES (?,?);", 'Matt', 'Finley']
mssqlManipulation(tsql)

# Insert Another Query
tsql = ['Inserting a new row into table:', 'Successfully Inserted!',
        "INSERT INTO Employees (Name, Location) VALUES (?,?);", 'Victor', 'Waking']
mssqlManipulation(tsql)

# Update Existing Query
tsql = ['Updating Location for Malik:', 'Successfully Updated!',
        "UPDATE Employees SET Location = ? WHERE Name = ?", 'Southminster', 'Malik']
mssqlManipulation(tsql)

# Update Existing Query
tsql = ['Updating Name of employee:', 'Successfully Updated!',
        "UPDATE Employees SET Name = ? WHERE Location = ?", 'Aha', 'Basildon']
mssqlManipulation(tsql)

# Delete Query
tsql = ['Deleting user Sam:', 'Successfully Deleted!',
        "DELETE FROM Employees WHERE Name = ?", 'Sam']
mssqlManipulation(tsql)

# Read Query from the table Employees
print('Reading data from table:')
tsql = "SELECT Name, Location FROM Employees;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print(f"{str(row[0])}  {str(row[1])}")
        row = cursor.fetchone()

# Close the connection.
conn.close()
print("Server connection closed.")
