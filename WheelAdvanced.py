import random

def roulette_generator():
  # Create a list of roulette numbers
  roulette_numbers = [i for i in range(37)]
  # Add 00 to the list
  roulette_numbers.append("00")

  # Create a dictionary mapping numbers to colors
  colors = {
      0: "green",
      1: "red",
      2: "black",
      3: "red",
      4: "black",
      5: "red",
      6: "black",
      7: "red",
      8: "black",
      9: "red",
      10: "black",
      11: "black",
      12: "red",
      13: "black",
      14: "red",
      15: "black",
      16: "red",
      17: "black",
      18: "red",
      19: "red",
      20: "black",
      21: "red",
      22: "black",
      23: "red",
      24: "black",
      25: "red",
      26: "black",
      27: "red",
      28: "black",
      29: "black",
      30: "red",
      31: "black",
      32: "red",
      33: "black",
      34: "red",
      35: "black",
      36: "red",
      "00": "green"
  }

  # Randomly select a number from the list
  result = random.choice(roulette_numbers)
  # Get the color of the result
  color = colors[result]

  return result, color

# Initialize an empty list to store the results
results = []

print("Welcome to the PYTHON CASINO!")

# Run the roulette generator until the user wants to stop
while True:
  # Generate a roulette result
  result, color = roulette_generator()
  # Add the result to the list of results
  results.append((result, color))
  # Only keep the last 5 results
  results = results[-5:]

  # Print the result and the past 5 results
  print(f"Result: {result} ({color})")
  print("Past results:")
  for past_result, past_color in results:
    print(f"  {past_result} ({past_color})")

  # Prompt the user to continue or stop
  user_input = input("Enter 'c' to continue or 's' to stop: ")
  if user_input == 's':
    break
