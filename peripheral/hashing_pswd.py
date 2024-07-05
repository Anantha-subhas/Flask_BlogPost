"""
In Flask, you can use the bcrypt library to hash and verify passwords securely. 
Bcrypt is a popular password hashing algorithm designed to be slow 
and computationally intensive, making it resistant to brute-force attacks.
"""

# pip install Flask-Bcrypt


from flask_bcrypt import Bcrypt

# When a user registers or updates their password, you should hash the password
# using bcrypt before storing it in the database. Here's an example:


bcrypt = Bcrypt()

password = "user_password"
hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
print(hashed_password)
# Store the 'hashed_password' in your database
