"""
Verifying Passwords:
When a user logs in, you should verify the entered password against the stored hashed password. Here's an example:
"""


from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Retrieve the hashed password from your database
stored_hashed_password = "$2b$12$AfSYpKdlG4T2/rrpBq2ycOAr3/5rjDEp3G9M4pNbqYl3E7sEiyrD2"

# User enters password during login
entered_password = "user_password"

if bcrypt.check_password_hash(stored_hashed_password, entered_password):
    # Passwords match, allow access
    print("Password is correct")
else:
    # Passwords do not match, deny access
    print("Incorrect password")
