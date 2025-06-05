import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name):
    """
    Fetches animal data for the given name from the API.
    Returns: list of animal dictionaries or empty list if failed.
    """
    try:
        response = requests.get(
            f"https://api.api-ninjas.com/v1/animals?name={animal_name}",
            headers={"X-Api-Key": API_KEY}
        )
        return response.json() if response.status_code == 200 else []
    except Exception as e:
        print("Error fetching data:", e)
        return []
