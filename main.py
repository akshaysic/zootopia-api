import os
from dotenv import load_dotenv
import requests

# Load the API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Ask user for animal name
animal_name = input("Enter a name of an animal: ")

# Make API request
response = requests.get(
    f"https://api.api-ninjas.com/v1/animals?name={animal_name}",
    headers={"X-Api-Key": API_KEY}
)

# Parse response
animals = response.json()

# Generate HTML file
with open("animals.html", "w") as f:
    f.write("<html><body>\n")
    f.write(f"<h1>Animal Search: {animal_name}</h1>\n")

    if animals:
        for animal in animals:
            f.write(f"<h2>{animal['name']}</h2>\n")
            f.write(f"<p><strong>Diet:</strong> {animal['characteristics']['diet']}</p>\n")
            f.write(f"<p><strong>Habitat:</strong> {animal['characteristics']['habitat']}</p>\n")
            f.write("<hr>\n")
    else:
        f.write(f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>\n")

    f.write("</body></html>")

print("Website was successfully generated to the file animals.html.")
