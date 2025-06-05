# Zootopia API

This is a Python program that fetches animal data from the API Ninjas Animals API and creates a simple HTML website to display the information.

## About

You can enter an animal name (like "fox" or "lion"), and the program will generate an `animals.html` file showing details like diet and habitat.

If the animal name is not found, the website will show a message saying that the animal does not exist.

## Running the Program

If you are running this in Codio or another new environment, make sure to do the following steps:

### 1. Install Required Libraries

Run this in the terminal to install the packages used by the program:

pip install -r requirements.txt


This will install:

- `requests` (used to call the API)
- `python-dotenv` (used to load your API key from a .env file)

### 2. Create a `.env` File

This file should be in the same folder as your Python script.

Example `.env` content:

API_KEY='your_api_key_here'


Replace `'your_api_key_here'` with your actual API key from API Ninjas.

### 3. Run the Script

Run the script using:

python3 animals_web_generator.py


You will be asked to enter an animal name. Then the program will create a file called `animals.html`.

You can open `animals.html` in a browser to see the results.

## Notes

- Do not forget to create the `.env` file each time you work in a new environment like Codio.
- The `.env` file is ignored by Git for security reasons.
