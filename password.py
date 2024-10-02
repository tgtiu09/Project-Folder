# Write here you solution for the 02-password exercise

# Prompt the user to enter a password
p = input ("Create a password: ")
# Prompt the user to confirm the password
conf = input ("Confirm your password: ")
# Check if the password and confirmation match
if p == conf:
    print ("Passwords match.")
else:
    print ("Passwords do not match.")