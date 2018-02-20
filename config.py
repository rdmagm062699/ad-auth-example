import os, random

def get_random_string(length=12, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    my_random = random.SystemRandom()
    return ''.join(my_random.choice(allowed_chars) for i in range(length))

def get_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
THREADS_PER_PAGE = 2
CSRF_ENABLED     = False
CSRF_SESSION_KEY = get_secret_key()
SECRET_KEY = get_secret_key()
