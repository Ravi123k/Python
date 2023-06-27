import random

# List of possible locations
locations = ['forest', 'desert', 'mountain', 'cave']

# Choose a random starting location
location = random.choice(locations)

print("You find yourself in a", location)

# The player starts with 100 health points
health = 100

# The player starts with an empty inventory
inventory = []

# This is the main game loop
while True:
  # Print the player's current status
  print("You are in a", location)
  print("Your health is", health)
  print("Your inventory is", inventory)
  
  # Print the available actions
  print("What do you want to do?")
  print("  1. Move to a new location")
  print("  2. Find food")
  print("  3. Find a weapon")
  print("  4. Fight an enemy")
  print("  5. Quit the game")
  
  # Get the player's choice
  choice = int(input("> "))
  
  # Handle the player's choice
  if choice == 1:
    # Move to a new location
    location = random.choice(locations)
  elif choice == 2:
    # Find some food
    if 'food' in location:
      print("You found some food!")
      inventory.append('food')
    else:
      print("There is no food here.")
  elif choice == 3:
    # Find a weapon
    if 'weapon' in location:
      print("You found a weapon!")
      inventory.append('weapon')
    else:
      print("There is no weapon here.")
  elif choice == 4:
    # Fight an enemy
    if 'enemy' in location:
      print("You fought an enemy and won!")
      locations.remove('enemy')
    else:
      print("There is no enemy here.")
  elif choice == 5:
    # Quit the game
    print("Thank you for playing!")
    break
  else:
    # Invalid choice
    print("Invalid choice. Try again.")




