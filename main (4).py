# Student Information Formatter
# Version 2 - String Formatting

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

# Combine and format the full name
full_name = first_name.title() + " " + last_name.title()

# Display formatted output
print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section.upper())
print("Favorite Subject:", favorite_subject.title())
print("Character Count:", len(full_name))