import sqlite3
from student_account import StudentAccount

class DBManager:
    def __init__(self, db_path=""):
        # Set up any necessary instance variables.
        # By default the db_path is empty, but we may send one during instantiation like so: db_manager = DBManager("../data/")
        self._db = db_path + "/" + "cse2050_students_db.db"
        self._conn = None  # no connection is made upon instantiation
        self._cursor = None

    # Note that it is good practice to open and close connections every time you complete a transaction on a DB
    def open_connection(self):
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()

    def close_connection(self):
        self._conn.close()

    # This method is expected to create the table and load the initial data into the database
    def init_tables(self):
        names = ["Willena Shupe", "Jolanda Agin", "Leta Stacker",
                 "Leonora Oliverio", "Birgit Stoudt", "Aron Valtierra", "Vi Buschman",
                 "Janee Barnwell", "Agnus Flower", "Byron Mccartney",
                 "Victoria Crabill", "Amy Swinton", "Arla Mohamed", "Bryon Vester",
                 "Lue Benway", "Mozelle Macauley", "Suzann Galindo",
                 "Delicia Barriere", "Marcella Uyehara", "Jane Curley"]

        admittance_years = [2020, 2019, 2016, 2019, 2013, 2014, 2014, 2018, 2016, 2012,
                            2014, 2015, 2018, 2013, 2019, 2017, 2019, 2020, 2015, 2013]

        # Drops previous table
        self._cursor.execute(""" DROP TABLE IF EXISTS Students """)

        # Creates table with columns
        self._cursor.execute("""
        CREATE TABLE Students (
        student_id INTEGER,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        email_address VARCHAR(200),
        admittance_year INTEGER,
        photo VARCHAR(300)
        )""")

        # Loops through list of names and years and fills db with students
        for i in range(len(names)):
            users = {'first': names[i].split()[0], 'last': names[i].split()[1], 'year': admittance_years[i]}

            stud = StudentAccount(users['first'], users['last'], users['year'])        # Creates student account for each student


            self._cursor.execute("""INSERT INTO Students (student_id,first_name,last_name,email_address,admittance_year,photo) 
                                    VALUES (:id, :first, :last, :email, :year, :photo)""", stud.user)
        self._conn.commit()

    # Adds new student record to database
    def add_record(self, record):
        new_stud = StudentAccount(record[0], record[1], record[2])    # Creates new student with record which creates all data needed

        query = """INSERT INTO Students VALUES (:id, :first, :last, :email, :year, :photo)"""

        try:
            self._cursor.execute(query, new_stud.user)
            self._conn.commit()
        except Exception:
            raise Exception

    # Search database by student ID, fetches first
    def search_by_id(self, student_id):
        sql_search_id = f"SELECT * FROM Students WHERE student_id='{student_id}'"
        self._cursor.execute(sql_search_id)
        result = self._cursor.fetchone()
        return result

    # Searches the database by student name
    def search_by_name(self, student_name):
        # return one or more records that match the criteria given on the assignment
        sql_search_name = f"SELECT * FROM Students WHERE first_name LIKE '%{student_name}%' OR last_name LIKE '%{student_name}%'"
        self._cursor.execute(sql_search_name)
        result = self._cursor.fetchall()
        return result
