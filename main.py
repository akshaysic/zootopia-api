import os
from dotenv import load_dotenv
import requests

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Preset animal list
preset_animals = ["Cat", "Dog", "Fox", "Lion", "Elephant", "Monkey", "Tiger"]

# Ask user to pick method
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
        while True:
            animal_name = input("Enter a name of an animal: ").strip()
            if animal_name:
                break
            print("Please enter a valid animal name.\n")
        break
    else:
        print("Invalid option. Please try again.\n")

# Fetch data until valid result is found
while True:
    response = requests.get(
        f"https://api.api-ninjas.com/v1/animals?name={animal_name}",
        headers={"X-Api-Key": API_KEY}
    )

    try:
        animals = response.json()
    except Exception as e:
        print("Error parsing API response:", e)
        animals = []

    if isinstance(animals, list) and animals:
        animals = animals[:10]  # Limit to 10
        break
    else:
        print(f'Sorry, no animals were found for "{animal_name}". Please try again.\n')
        animal_name = input("Enter a name of an animal: ").strip()

# Generate HTML
with open("animals.html", "w") as f:
    f.write("<html><head><title>Zootopia Results</title>\n")
    f.write("<style>\n")
    f.write("body { font-family: Arial, sans-serif; margin: 20px; }\n")
    f.write("section { border: 1px solid #ccc; padding: 10px; margin-bottom: 15px; border-radius: 8px; }\n")
    f.write("h1 { color: #2c3e50; }\n")
    f.write("h2 { color: #16a085; }\n")
    f.write("</style>\n</head><body>\n")

    f.write(f"<h1>Animal Search: {animal_name}</h1>\n")

    for animal in animals:
        f.write("<section>\n")
        f.write(f"<h2>{animal.get('name', 'Unknown')}</h2>\n")
        characteristics = animal.get('characteristics', {})
        f.write(f"<p><strong>Diet:</strong> {characteristics.get('diet', 'Unknown')}</p>\n")
        f.write(f"<p><strong>Habitat:</strong> {characteristics.get('habitat', 'Unknown')}</p>\n")
        f.write(f"<p><strong>Top Speed:</strong> {characteristics.get('top_speed', 'Unknown')}</p>\n")
        f.write("</section>\n")

    f.write("</body></html>")

print("Website was successfully generated to the file animals.html.")
