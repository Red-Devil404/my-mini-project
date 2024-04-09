from database import PeopleList

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

