import random
import string

def suggest_password(keyword, use_uppercase=True, use_numbers=True, use_symbols=True):
    substitutions = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7', 'b': '8', 'g': '9', 'l': '1'}

    # Substitute characters based on the substitution dictionary and remove spaces
    password = ''.join(substitutions.get(char.lower(), char) for char in keyword if char != ' ')

    # Ensure the password contains at least one uppercase letter if requested
    if use_uppercase and not any(char.isupper() for char in password):
        password += random.choice(string.ascii_uppercase)

    # Ensure the password contains at least one digit if requested
    if use_numbers and not any(char.isdigit() for char in password):
        password += random.choice(string.digits)

    # Ensure the password contains at least one special character if requested
    if use_symbols and not any(char in string.punctuation for char in password):
        password += random.choice(string.punctuation)

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)

    # Ensure the password is at least 8 characters long
    while len(final_password) < 8:
        final_password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    # Shuffle again to mix the newly added characters
    password_list = list(final_password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)

    # Trim the final password to match the length of the keyword or be at least 8 characters long
    final_length = max(len(keyword.replace(' ', '')), 8)
    final_password = final_password[:final_length]

    # Ensure the final password contains at least one uppercase, one lowercase, one digit, and one special character
    if use_uppercase and not any(char.isupper() for char in final_password):
        final_password += random.choice(string.ascii_uppercase)
    if not any(char.islower() for char in final_password):
        final_password += random.choice(string.ascii_lowercase)
    if use_numbers and not any(char.isdigit() for char in final_password):
        final_password += random.choice(string.digits)
    if use_symbols and not any(char in string.punctuation for char in final_password):
        final_password += random.choice(string.punctuation)

    # Shuffle one last time to mix in the added characters
    password_list = list(final_password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)

    return final_password[:final_length]

def main():
    try:
        keyword = input("Enter a keyword idea for your password: ")
        use_uppercase = input("Do you want to include uppercase letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Do you want to include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Do you want to include symbols? (yes/no): ").lower() == 'yes'
        
        password = suggest_password(keyword, use_uppercase, use_numbers, use_symbols)
        print(f"Suggested Password: {password}")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
