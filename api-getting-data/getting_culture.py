import requests
import json
import os
import apikey

EUROPEANA_API_KEY = os.getenv("EUROPEANA_API_KEY") 
def get_europeana(query):
    euurl = "https://api.europeana.eu/record/v2/search.json"
    params = {
        'wskey': "EUROPEANA_API_KEY",
        'query': query
    }
def get_bisexuals():
    url = 'https://en.wikipedia.org/wiki/List_of_bisexual_characters_in_television'
    response = requests.get(url)
    if response.status_code == 200:
        bisexual_character = response.json()
        print("Bisexual Character:",bisexual_character)
        return bisexual_character
    else:
        print("Could not retrieve API")
    
def main():
    bisexual_character = get_bisexuals()
    if not bisexual_character:
        return
    data = {
        "bisexual character":bisexual_character["data"]

    }
    my_file = f"bisexualsandeuropeana.json"
    with open(file, 'w') as file:
        json.dump(data, file)
    print(f"The bisexual character has been saved to {file}")

    if __name__ == "__main__":
        return