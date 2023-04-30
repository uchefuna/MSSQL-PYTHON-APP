

def mssqlConnectionStringDB():
    mssqlString = None
    try:
        driver = "{ODBC Driver 17 for SQL Server}"
        server = "XXXXXX\\SQLDEVELOPER"
        database = "SamplePython"
        username = "your_usernamr"
        password = "your_password"
        mssqlString = "DRIVER=" + driver + ";SERVER=" + server + \
            ";DATABASE=" + database + ";UID=" + username + ";PWD=" + password
    except ValueError as err:
        print(f"Error: '{err}'")
    else:
        print("MSSQL Database connection successful")
    return mssqlString
