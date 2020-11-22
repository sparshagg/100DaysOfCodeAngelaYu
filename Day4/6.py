# Assignment - https://repl.it/@appbrewery/day-4-3-exercise#README.md
# Treasure Map


treasure_list = [["⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️"]]
print(treasure_list[0])
print(treasure_list[1])
print(treasure_list[2])
location = input("Where do you want to put the trasure? \n")
treasure_list[int(location[1])-1][int(location[0])-1] = "X"
print(treasure_list[0])
print(treasure_list[1])
print(treasure_list[2])
