import requests

# Make a GET request to the Pokémon API
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the name and abilities
    name = data["name"]
    abilities = [ability["ability"]["name"] for ability in data["abilities"]]

    # Print the name and abilities
    print(f"Name: {name}")
    print(f"Abilities: {abilities}")

else:
    print(f"Error: {response.status_code}")
