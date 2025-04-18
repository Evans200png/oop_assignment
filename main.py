# loading the pet and creating ann object
from pet import Pet

# creating a pet
my_pet = Pet("Evans")

# Calling methods
my_pet.get_status()
my_pet.eat()
my_pet.sleep()
my_pet.play()

# teach and show tricks
my_pet.train("roll over")
my_pet.train("sit")
my_pet.show_tricks()

# Final status
my_pet.get_status()
