# random_number_generator.py

import random

def generate_random_number(start, end):
    """
    Generates a random number between the specified start and end values.
    
    Args:
    - start (int): The start of the range (inclusive).
    - end (int): The end of the range (inclusive).
    
    Returns:
    - int: The randomly generated number.
    """
    return random.randint(start, end)

def main():
    print("Welcome to the Random Number Generator!")
    
    # Get user input for the range
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    # Generate a random number
    random_number = generate_random_number(start, end)
    
    # Display the result
    print(f"Random number between {start} and {end}: {random_number}")

if __name__ == "__main__":
    main()
