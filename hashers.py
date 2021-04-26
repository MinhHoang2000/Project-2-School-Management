from django.contrib.auth.hashers import PBKDF2PasswordHasher

class MyPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    """
    A subclass of PBKDF2PasswordHasher that uses 50 times more iterations.
    """
    iterations = PBKDF2PasswordHasher.iterations * 50