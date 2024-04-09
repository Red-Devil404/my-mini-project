import mysql.connector

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PeopleList:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="ODBC",
            password="admin",
            database="people_db"
        )
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS People (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT
            )
        """)
        self.conn.commit()

    def add_person(self, name, age):
        person = Person(name, age)
        sql = "INSERT INTO People (name, age) VALUES (%s, %s)"
        val = (person.name, person.age)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def show_people(self):
        self.cursor.execute("SELECT * FROM People")
        result = self.cursor.fetchall()
        for row in result:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
            
    def search_person(self, name):
        # Search for a person by name in the database and display their details if found
        sql = "SELECT * FROM People WHERE name = %s"
        val = (name,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result:
            print(f"Person found - Name: {result[1]}, Age: {result[2]}")
        else:
            print("Person not found.")
            
          
    def filter_people_by_age(self, min_age, max_age):
        # Filter people by age in the database and display their details
        sql = "SELECT * FROM People WHERE age BETWEEN %s AND %s"
        val = (min_age, max_age)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchall()
        if result:
            print("People whose age is between {} and {}:".format(min_age, max_age))
            for person in result:
                print("Name: {}, Age: {}".format(person[1], person[2]))
        else:
            print("No people found with the specified age range.")

    def __del__(self):
        self.cursor.close()
        self.conn.close()
