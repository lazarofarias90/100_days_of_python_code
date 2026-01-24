import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# First Option
print(random.choice(friends))

# Second Option
random_position = random.randint(0, 4)
print(friends[random_position])