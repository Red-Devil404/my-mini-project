from database import PeopleList

  ###### PART1 ######

people_list = PeopleList()

# Add people to the list
people_list.add_person("Alice", 30)
people_list.add_person("Bob", 25)

# Show all people in the list
people_list.show_people()

# Search for a person by name
people_list.search_person("Alice")
people_list.search_person("Bob")
people_list.search_person("Charlie")

# Filter people by age
people_list.filter_people_by_age(20, 30)  # Example: Retrieve people aged between 20 and 30


from database import QueueWait

# Create an instance of QueueWait
queue_manager = QueueWait()

# Add a person to the queue
queue_manager.add_person_waiting("John Doe")

# Remove the first person from the queue
queue_manager.remove_waiting_person()


from database import QueueWait

# Create an instance of QueueWait
queue_manager = QueueWait()

# Add a priority person to the queue
queue_manager.add_priority_person("Jane Doe")

# Remove a person from the queue based on priority
queue_manager.remove_waiting_person()


from database import SalleCinema

# Create an instance of SalleCinema
cinema = SalleCinema()

# Reserve a place for a person
cinema.reserver_place("John Doe", "A1")

# Display reserved places
cinema.display_reserved_places()


      ###### PART2 ######

from database import SalleCinema

# Create an instance of SalleCinema
cinema = SalleCinema()

# Display the number of available seats
cinema.number_places_available()

# Reserve a place for a person
cinema.reserver_place("John Doe", "A1")




from database import SalleCinema

# Create an instance of SalleCinema
cinema = SalleCinema()

# Filter reservations by a specific person
cinema.filter_reservations_by_person("John Doe")



from database import SalleCinema

# Create an instance of SalleCinema
cinema = SalleCinema()

# Cancel reservations made by a specific person
cinema.cancel_reservation("John Doe")



from database import SalleCinema

# Create an instance of SalleCinema
cinema = SalleCinema()

# Reserve a special place for a disabled person
cinema.reserver_place_speciale("Jane Doe")






