import os
from dotenv import load_dotenv
import requests

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Offer menu until valid input is received
preset_animals = ["Cat", "Dog", "Fox", "Lion", "Elephant", "Monkey", "Tiger"]

while True:
    print("Choose an option:")
    print("1. Select from a list")
    print("2. Type an animal name")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("Available animals:")
        for i, animal in enumerate(preset_animals, start=1):
            print(f"{i}. {animal}")
        selected = input("Enter the number of the animal: ")
        if selected.isdigit() and 1 <= int(selected) <= len(preset_animals):
            animal_name = preset_animals[int(selected) - 1]
            break
        else:
            print("Invalid number. Please try again.\n")
    elif choice == "2":
        animal_name = input("Enter a name of an animal: ").strip()
        if animal_name:
            break
        else:
            print("Please enter a valid name.\n")
    else:
        print("Invalid option. Please try again.\n")

# API request
response = requests.get(
    f"https://api.api-ninjas.com/v1/animals?name={animal_name}",
    headers={"X-Api-Key": API_KEY}
)

try:
    animals = response.json()
except Exception as e:
    print("Error parsing API response:", e)
    animals = []

# Create HTML
with open("animals.html", "w") as f:
    f.write("<html><body>\n")
    f.write(f"<h1>Animal Search: {animal_name}</h1>\n")

    if isinstance(animals, list) and animals:
        for animal in animals:
            f.write(f"<h2>{animal['name']}</h2>\n")
            f.write(f"<p><strong>Diet:</strong> {animal['characteristics']['diet']}</p>\n")
            f.write(f"<p><strong>Habitat:</strong> {animal['characteristics']['habitat']}</p>\n")
            f.write("<hr>\n")
    else:
        f.write(f"<h2>The animal \"{animal_name}\" doesn't exist or no data was found.</h2>\n")

    f.write("</body></html>")

print("Website was successfully generated to the file animals.html.")
