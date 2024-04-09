import mysql.connector

###### PART1 ######

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PeopleList:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
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
            
            
          
class QueueWait:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="people_db"
        )
        self.cursor = self.conn.cursor()

    def add_person_waiting(self, name):
        sql_insert_query = "INSERT INTO FileAttente (name) VALUES (%s)"
        person_data = (name,)
        self.cursor.execute(sql_insert_query, person_data)
        self.conn.commit()

    def remove_waiting_person(self):
        sql_select_query = "SELECT name FROM FileAttente LIMIT 1"
        self.cursor.execute(sql_select_query)
        first_person = self.cursor.fetchone()
        if first_person:
            print("Removed from queue:", first_person[0])
            sql_delete_query = "DELETE FROM FileAttente WHERE name = %s"
            self.cursor.execute(sql_delete_query, (first_person[0],))
            self.conn.commit()
        else:
            print("Queue is empty")


class QueueWait:
    def __init__(self):
        # Initialize the connection to the database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="people_db"
        )
        self.cursor = self.conn.cursor()

    def add_priority_person(self, name):
        # Add a priority person to the queue in the database
        sql_insert_query = "INSERT INTO FileAttente (name, priority) VALUES (%s, %s)"
        person_data = (name, "priority")  # Assuming "priority" is a flag indicating priority
        self.cursor.execute(sql_insert_query, person_data)
        self.conn.commit()

    def remove_waiting_person(self):
        # Remove a person from the queue in the database based on priority
        # First, check if there are any priority persons in the queue
        sql_select_priority_query = "SELECT name FROM FileAttente WHERE priority = %s LIMIT 1"
        self.cursor.execute(sql_select_priority_query, ("priority",))
        priority_person = self.cursor.fetchone()

        if priority_person:
            # If a priority person exists, delete them from the queue
            print("Removed priority person:", priority_person[0])
            sql_delete_query = "DELETE FROM FileAttente WHERE name = %s"
            self.cursor.execute(sql_delete_query, (priority_person[0],))
            self.conn.commit()
        else:
            # If no priority person exists, delete the first normal person
            sql_select_normal_query = "SELECT name FROM FileAttente LIMIT 1"
            self.cursor.execute(sql_select_normal_query)
            normal_person = self.cursor.fetchone()
            if normal_person:
                print("Removed normal person:", normal_person[0])
                sql_delete_query = "DELETE FROM FileAttente WHERE name = %s"
                self.cursor.execute(sql_delete_query, (normal_person[0],))
                self.conn.commit()
            else:
                print("Queue is empty")

# Replace "priority" with your actual values.



class SalleCinema:
    def __init__(self):
        # Initialize the connection to the database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="people_db"
        )
        self.cursor = self.conn.cursor()

    def reserver_place(self, name, place):
        # Reserve a place for a person and save the reservation in the database
        sql_insert_query = "INSERT INTO Reservations (name, place) VALUES (%s, %s)"
        reservation_data = (name, place)
        self.cursor.execute(sql_insert_query, reservation_data)
        self.conn.commit()

    def display_reserved_places(self):
        # Display the places reserved by retrieving data from the Reservations table
        sql_select_query = "SELECT name, place FROM Reservations"
        self.cursor.execute(sql_select_query)
        reservations = self.cursor.fetchall()
        if reservations:
            for reservation in reservations:
                print("Name:", reservation[0], "- Place:", reservation[1])
        else:
            print("No reservations found")




###### PART2 ######

class SalleCinema:
    def __init__(self):
        # Initialize the connection to the database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="people_db"
        )
        self.cursor = self.conn.cursor()

    def number_places_available(self):
        # Display the number of available seats by consulting the Reservations table
        sql_select_query = "SELECT COUNT(*) FROM Reservations"
        self.cursor.execute(sql_select_query)
        total_reservations = self.cursor.fetchone()[0]
        total_seats = 100  # Assuming there are 100 seats in the cinema
        available_seats = total_seats - total_reservations
        print("Number of available seats:", available_seats)

    def reserver_place(self, name, place):
        # Check if there are still places available in the room
        self.number_places_available()

        # Reserve a place for a person if there are available seats
        if self.number_places_available > 0:
            sql_insert_query = "INSERT INTO Reservations (name, place) VALUES (%s, %s)"
            reservation_data = (name, place)
            self.cursor.execute(sql_insert_query, reservation_data)
            self.conn.commit()
            print("Reservation successful!")
        else:
            print("No available seats. Reservation failed.")



class SalleCinema:
    def __init__(self):
        # Initialize the connection to the database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="people_db"
        )
        self.cursor = self.conn.cursor()

    def filter_reservations_by_person(self, name):
        # Display reservations made by a specific person
        sql_select_query = "SELECT place FROM Reservations WHERE name = %s"
        self.cursor.execute(sql_select_query, (name,))
        reservations = self.cursor.fetchall()
        if reservations:
            print("Reservations made by {}:".format(name))
            for reservation in reservations:
                print("Place:", reservation[0])
        else:
            print("No reservations found for {}".format(name))



class SalleCinema:
    def __init__(self):
        # Initialize the connection to the database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="people_db"
        )
        self.cursor = self.conn.cursor()

    def cancel_reservation(self, name):
        # Cancel all reservations made by a specific person
        sql_delete_query = "DELETE FROM Reservations WHERE name = %s"
        self.cursor.execute(sql_delete_query, (name,))
        self.conn.commit()
        print("Reservations cancelled for", name)


class SalleCinema:
    def __init__(self):
        # Initialize the connection to the database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="people_db"
        )
        self.cursor = self.conn.cursor()

    def reserver_place_speciale(self, name):
        # Reserve a special place for a disabled person
        sql_insert_query = "INSERT INTO Reservations (name, place_type) VALUES (%s, 'special')"
        reservation_data = (name,)
        self.cursor.execute(sql_insert_query, reservation_data)
        self.conn.commit()
        print("Special place reserved for", name)


          
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        
        
    
