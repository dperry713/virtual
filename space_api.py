
import requests

def fetch_planet_data():
    # API endpoint for fetching planet data
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
    # Send GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        planets = response.json()['bodies']
        
        # Process and print information for each planet
        for planet in planets:
            if planet['isPlanet']:
                name = planet.get('englishName', 'Unknown')  # Get planet's English name
                mass = planet.get('mass', {}).get('massValue', 'N/A')  # Get mass value
                orbit_period = planet.get('sideralOrbit', 'N/A')  # Get orbital period
                
                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Execute the function to fetch and display planet data
fetch_planet_data()

