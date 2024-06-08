
# Password Generator Program

This program generates a secure password based on a keyword provided by the user. The user can choose whether to include uppercase letters, numbers, and symbols in the generated password. The password is randomized and modified to ensure security and meet the criteria specified by the user.

## Features

- Substitutes common letters with similar-looking symbols (e.g., 'a' becomes '@', 'e' becomes '3').
- Ensures the inclusion of uppercase letters, digits, and special characters based on user preferences.
- Randomizes the order of characters in the password.
- Ensures the password is at least 8 characters long.
- Provides a secure password that contains a mix of character types to enhance security.

## Usage

1. **Navigate to the project directory**:
    ```bash
    cd password-gen-program
    ```

2. **Run the Password Suggestion Program**:
    ```bash
    python password_gen.py
    ```

3. **Follow the prompts**:
    - Enter a keyword when prompted. This keyword will form the base of the password.
    - Specify whether to include uppercase letters, numbers, and symbols by answering 'yes' or 'no' to the prompts.
    - The program will generate and display a secure password based on your preferences.

### Example

```bash
Enter a keyword idea for your password: password
Do you want to include uppercase letters? (yes/no): yes
Do you want to include numbers? (yes/no): yes
Do you want to include symbols? (yes/no): yes
Suggested Password: @7S0p9$
```

## Files

- `password_gen.py`: Contains the main script and functions to generate the password.
- `README.md`: This file, providing an overview and instructions for the program.

## Functions

### `suggest_password`

Generates a password based on the provided keyword and user preferences.

**Parameters**:

- `keyword` (str): The base keyword for the password.
- `use_uppercase` (bool): Whether to include uppercase letters.
- `use_numbers` (bool): Whether to include numbers.
- `use_symbols` (bool): Whether to include special characters.

**Returns**:

- `str`: A generated password.

### `main`

Handles user input and calls the `suggest_gen` function to generate and display the password.

## Running the Program

To run the program, use the following command:

```bash
python password_gen.py
```

Follow the on-screen prompts to generate your password.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---


