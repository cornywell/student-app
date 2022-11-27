# student-app

To get this application up and running for development run the following:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask --app app.py --debug run
```

Database
database.db is an instance of sqlite to query the db run the following:
enter sqlite shell:
```
sqlite3 database.db
```

list tables:
```
.tables
```

query student table:
```
SELECT * FROM student;
```

quit:
```
.quit
```

Forgive me for the structure of the application and the lack of testing.
