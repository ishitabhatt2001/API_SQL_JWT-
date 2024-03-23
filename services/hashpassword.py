import bcrypt

def generate_hash_password(plaintext_password):
    # Generate a unique salt
    salt = bcrypt.gensalt()
    # Hash the plaintext password with the salt
    hashed_password = bcrypt.hashpw(plaintext_password.encode('utf-8'), salt)
    salt = salt.decode('utf-8')
    hashed_password = hashed_password.decode('utf-8')
    return salt , hashed_password
