import requests

# Fetch planet data from the Solar System OpenData API
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = []

    if response.status_code == 200:
        bodies = response.json()['bodies']
        # Filter and extract relevant data for planets
        for body in bodies:
            if body['isPlanet']:
                planet_info = {
                    'name': body.get('englishName', 'Unknown'),
                    'mass': body.get('mass', {}).get('massValue', 0),
                    'orbit_period': body.get('sideralOrbit', 0)
                }
                planets.append(planet_info)
    else:
        print(f"Failed to fetch data: {response.status_code}")
    return planets

# Find the heaviest planet based on mass
def find_heaviest_planet(planets):
    heaviest = max(planets, key=lambda p: p['mass'])
    return heaviest['name'], heaviest['mass']

# Fetch planet data
planets = fetch_planet_data()

# Analyze to find the heaviest planet
name, mass = find_heaviest_planet(planets)

# Print the result
print(f"The heaviest planet is {name} with a mass of {mass} x10^24 kg.")
