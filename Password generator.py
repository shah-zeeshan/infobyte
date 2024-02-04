import string
import random

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Define character sets based on user preferences
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Check if at least one character set is selected
    if not characters:
        print("Error: Please select at least one character set.")
        return None

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("********** Password Generator **********")

    # Get user preferences
    length = int(input("Enter the length of the password: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    # Display the generated password
    if password:
        print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
