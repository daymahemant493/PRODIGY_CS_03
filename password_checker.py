import requests

def get_common_passwords_list():
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
    response = requests.get(url)
    return response.text.splitlines()

def check_password_strength(password, common_passwords):
    # define criteria
    min_length = 8
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in '@#$%^&*()_-+={}[]|\:;"<>,.?/~`' for char in password)
    not_common_password = password not in common_passwords

    # checking criteria
    is_strong_password = (
            len(password) >= min_length and
            has_lowercase and
            has_uppercase and
            has_digit and
            has_special_char and
            not_common_password
    )

    # giving feedback
    print("Password feedback:")
    if is_strong_password:
        print("Great job! Your password is strong.")
    else:
        if len(password) < min_length:
            print("- Password is too short.")
        if not has_lowercase or not has_uppercase:
            print("- Include both lowercase and uppercase letters for better security.")
        if not has_digit:
            print("- Include numbers for better security.")
        if not has_special_char:
            print("- Include special characters for better security.")
        if not_common_password:
            print("- Avoid using common passwords for better security.")

common_passwords_list = get_common_passwords_list()

# Ask the user for their password
user_password = input("Enter your password: ")
check_password_strength(user_password, common_passwords_list)