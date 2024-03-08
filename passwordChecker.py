import re


def has_repeated_letters(password):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
        return False


def check_password_strength(password):
    if len(password) < 8:
        return "Weak. Password should be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return "Weak. Include at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Weak. Include at least one lowercase letter."
    if not any(char.isnumeric() for char in password):
        return "Weak. Include at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>`~+=]", password):
        return "Weak. Include at least one special character."
    return "Strong. Password met every criteria."
    common_passwords = ["password", "Password", "12345678", "1234567890", "0987654321", "qwertyuiop", "1q2w3e4r",
                        "1q2w3e4r5t", "q1w2e3r4", "Aa123456", "Admin", "admin", "12345678910", "Unknown", "UNKNOWN",
                        "unknown", "Admin123", "admin123", "11111111", "00000000", "shitbird", "Shitbird"]
    if password.lower() in common_passwords:
        return "Weak. You have typed a commonly used password. Choose a more unique one."
    if has_repeated_letters(password):
        return "Weak. Avoid repeating characters in your password."


while True:
    password_to_check = input("Enter a password to check: ")
    result = check_password_strength(password_to_check)
    print(result)
    if "Strong" in result:
        break
