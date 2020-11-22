# Understanding the Offset and Appending items to the list.
# Python documents on Data Structures - https://docs.python.org/3/tutorial/datastructures.html
# For reference use this - https://repl.it/@appbrewery/day-4-list-practice#main.py

# Order in which the states joined the union of America
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
                     "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
                     "Alaska", "Hawaii"]
# Order in which lists are indexed
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])

# Order in which states are indexed from the end
print(states_of_america[-1])
print(states_of_america[-2])

# Lists are mutable
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# Adding an item to a list at the end
states_of_america.append("HelloWorldLand")
print(states_of_america)

# Adding multiple items to a list at once
states_of_america.extend(["Delhi", "Chandigarh", "Gurgaon"])
print(states_of_america)
