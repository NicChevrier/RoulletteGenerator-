import random

def roulette_generator():
  # Create a list of roulette numbers
  roulette_numbers = [i for i in range(37)]
  # Add 00 to the list
  roulette_numbers.append("00")

  # Randomly select a number from the list
  result = random.choice(roulette_numbers)
  return result

print(roulette_generator())
