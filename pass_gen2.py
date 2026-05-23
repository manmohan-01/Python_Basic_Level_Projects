import secrets
import string

pass_len = 15

# Make sure password has all character types
password = [
    secrets.choice(string.ascii_lowercase),
    secrets.choice(string.ascii_uppercase),
    secrets.choice(string.digits),
    secrets.choice(string.punctuation),
]

# Fill the rest randomly
charValues = string.ascii_letters + string.digits + string.punctuation
password += [secrets.choice(charValues) for _ in range(pass_len - 4)]

# Shuffle to mix the characters
secrets.SystemRandom().shuffle(password)

# Join into a string
password = ''.join(password)

print("Generated Password:", password)
