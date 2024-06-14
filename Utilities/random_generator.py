import random
import string


def random_email_generator(domain='example.com', length=5):
    """Generate a random email address."""
    return f"Test{''.join(random.choices(string.digits, k=length))}@{domain}"
