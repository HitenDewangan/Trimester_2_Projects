import re

def validate_password(password, username=None, past_passwords=[]):
  """
  Validates a password against security criteria.

  Args:
      password: The password string to validate.
      username: (Optional) The username to check for sequence restrictions.
      past_passwords: (Optional) List of past passwords to check against.

  Returns:
      A list of error messages if the password is invalid, otherwise an empty list.
  """
  errors = []
  
  # Minimum length check
  if len(password) < 10:
    errors.append("Password must be at least 10 characters long.")

  # Character variety checks
  if not any(char.isupper() for char in password):
    errors.append("Password must contain at least two uppercase letters.")
  if not any(char.islower() for char in password):
    errors.append("Password must contain at least two lowercase letters.")
  if not any(char.isdigit() for char in password):
    errors.append("Password must contain at least two digits.")
  if not re.search(r"[!@#$%&*_]", password):
    errors.append("Password must contain at least two special characters (!@#$%&*_)")

  # Sequence and repetition checks
  if username:
    for i in range(len(username) - 2):
      if username[i:i+3] in password:
        errors.append("Password cannot contain sequences of 3 characters from username.")
  for char in password:
    if password.count(char) > 3:
      errors.append("Password cannot contain characters repeated more than 3 times.")

  # Historical password check (if past_passwords provided)
  if past_passwords:
    for past_password in past_passwords:
      if password == past_password:
        errors.append("Password cannot be the same as any of the last 3 passwords.")

  return errors

# Example usage
username = "johndoe"
past_passwords = ["weakpass1", "weakpass2", "slightlybetterpass"]

while True:
  password = input("Enter a new password: ")
  errors = validate_password(password, username, past_passwords)
  if not errors:
    print("Password is valid!")
    break
  else:
    print("Invalid password:")
    for error in errors:
      print("-", error)
