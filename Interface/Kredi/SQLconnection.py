import pyodbc

connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-5CILQ1E;'
                            'Database=Bank;'
                            'Trusted_Connection=yes;'
                            )

cursor = connection.cursor()
