import random
import string

# Function to get user input for password length
def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get user input for character type preferences
def get_character_preferences():
    print("Select character types to include in the password:")
    print("1. Letters")
    print("2. Numbers")
    print("3. Symbols")
    
    while True:
        choices = input("Enter your choices as a comma-separated list (e.g., 1,2,3): ").split(',')
        character_set = ""
        valid_choices = {'1': string.ascii_letters, '2': string.digits, '3': string.punctuation}

        for choice in choices:
            choice = choice.strip()
            if choice in valid_choices:
                character_set += valid_choices[choice]
        
        if character_set:
            return character_set
        else:
            print("Invalid choices. Please select at least one valid option.")

# Function to generate a random password
def generate_password(length, character_set):
    return ''.join(random.choice(character_set) for _ in range(length))

# Main function to run the password generator
def main():
    print("Welcome to the Random Password Generator")

    # Get password length from the user
    length = get_password_length()

    # Get character preferences from the user
    character_set = get_character_preferences()

    # Generate the random password
    password = generate_password(length, character_set)

    # Display the generated password
    print(f"Your generated password is: {password}")

# Ensuring the script runs only when executed directly
if __name__ == "__main__":
    main()
