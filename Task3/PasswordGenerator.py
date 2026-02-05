import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase   # only small letters
    elif complexity == 2:
        characters = string.ascii_lowercase + string.ascii_uppercase  # small + capital
    elif complexity == 3:
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits  # letters + numbers
    elif complexity == 4:
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation  # all
    else:
        return "Invalid complexity choice!"

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


print("------ PASSWORD GENERATOR ------")

length = int(input("Enter password length: "))

print("\nSelect Password Complexity Level:")
print("1. Only lowercase letters")
print("2. Lowercase + Uppercase letters")
print("3. Letters + Numbers")
print("4. Letters + Numbers + Special Characters")

complexity = int(input("Enter your choice (1-4): "))

password = generate_password(length, complexity)

print("\nGenerated Password:", password)
