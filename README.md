### First install pyodbc
```bash
pip3 install pyodbc
```

### Edit your config file

Install [ODBC Driver 13 for SQL Server](https://www.microsoft.com/en-us/download/details.aspx?id=50420)

### Edit your config file
```python
class DbConnect:
    server = ''
    driver= '{ODBC Driver 13 for SQL Server}'
```

# Arguments be like:
```bash
database
username
password
```
