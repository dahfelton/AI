#Programmer: Billy Felton
#Date: 3.12.2024
#Program: Password Generator
#Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib

def hash_password(password, salt):
    # Combine password and salt
    salted_password = password.encode() + salt.encode()
    # Hash the combined string using SHA-256
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

def main():
    # Prompt the user for a password
    password = input("Enter your password: ")
    # Choose a salt (you can generate a random salt for better security)
    salt = "random_salt_here"  # Replace this with your salt
    # Hash the password with the chosen salt
    hashed_password = hash_password(password, salt)
    # Print the hashed password
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()

