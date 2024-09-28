import requests

def get_pokemon_data(pokemon_name):
    """Fetches data for a given Pokémon from the Pokémon API.

    Args:
        pokemon_name (str): The name of the Pokémon to fetch data for.

    Returns:
        dict: A dictionary containing the Pokémon's name, abilities, and weight.
    """

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "weight": data["weight"]
        }
    else:
        print(f"Error fetching data for {pokemon_name}: {response.status_code}")
        return None

def calculate_average_weight(pokemon_data):
    """Calculates the average weight of a list of Pokémon.

    Args:
        pokemon_data (list): A list of dictionaries, each containing Pokémon data.

    Returns:
        float: The average weight of the Pokémon in the list.
    """

    total_weight = sum(pokemon["weight"] for pokemon in pokemon_data)
    return total_weight / len(pokemon_data)

# Fetch data for three Pokémon
pokemon_names = ["pikachu", "charmander", "bulbasaur"]
pokemon_data = [get_pokemon_data(name) for name in pokemon_names]

# Calculate the average weight
average_weight = calculate_average_weight(pokemon_data)

# Print the results
for pokemon in pokemon_data:
    print(f"Name: {pokemon['name']}")
    print(f"Abilities: {pokemon['abilities']}")
    print(f"Weight: {pokemon['weight']}")
    print("-" * 20)

print(f"Average Weight: {average_weight}")
