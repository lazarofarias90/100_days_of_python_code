def drink_potion():
    potion_strength = 2  # This variable is LOCAL.
    print(potion_strength) # It works! The function can "look" outside.

drink_potion()
# print(potion_strength)  <-- This would cause an ERROR! The code outside the function doesn't see the potion.

player_health = 10  # This variable is GLOBAL.