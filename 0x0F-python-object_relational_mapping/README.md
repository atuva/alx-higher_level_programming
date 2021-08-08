## 0x0F-python-object_relational_mapping
Learning about ORMs

### 0-select_states.py
A script that lists all `states` from the database `hbtn_0e_0_usa`
* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`

### 1-filter_states.py
A script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`
* Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id

### 2-my_filter_states.py
A  script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
* should take 4 arguments: mysql username, mysql password, database name and state name searched
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id

### 3-my_safe_filter_states.py
A a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
* should take 4 arguments: mysql username, mysql password, database name and state name searched
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id

### 4-cities_by_state.py
A script that lists all cities from the database hbtn_0e_4_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by cities.id
* You can use only execute() once
