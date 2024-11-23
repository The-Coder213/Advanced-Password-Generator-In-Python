import random

# Function to get user input choices
def get_choices():
    upper_case_letters = input("Do you want Uppercase Letters (Yes/No)? ").strip().lower()
    lower_case_letters = input("Do you want Lowercase Letters (Yes/No)? ").strip().lower()
    numbers = input("Do you want Numbers (Yes/No)? ").strip().lower()
    special_characters = input("Do you want Special Characters (Yes/No)? ").strip().lower()
    
    # List of available character types
    all_chars = []

    # Add character sets based on user input
    if upper_case_letters == "yes":
        all_chars.append("uppercase")
    if lower_case_letters == "yes":
        all_chars.append("lowercase")
    if numbers == "yes":
        all_chars.append("nums")
    if special_characters == "yes":
        all_chars.append("specials")
    
    return all_chars

# Function to generate the password
def generate_password(all_chars, password_length):
    # Character sets
    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    special_chars = "!£$%^&*()[]:;@'/?.><,|\\¬¦`"

    password = ""

    # Loop to generate the password
    for _ in range(password_length):
        random_selection = random.choice(all_chars)

        if random_selection == "uppercase":
            password += random.choice(uppercase_chars)
        elif random_selection == "lowercase":
            password += random.choice(lowercase_chars)
        elif random_selection == "nums":
            password += random.choice(numbers)
        elif random_selection == "specials":
            password += random.choice(special_chars)

    return password

# Main function to get choices and generate password
def main():
    # Get choices from the user
    all_chars = get_choices()

    if not all_chars:
        print("You must select at least one character type!")
        return

    # Get password length from user
    password_length = int(input("Enter Password Length: "))

    # Generate and print the password
    password = generate_password(all_chars, password_length)
    print(f"Your generated password is: {password}")

# Run the main function
if __name__ == "__main__":
    main()
