import requests # type: ignore
import json

# Overpass API endpoint
overpass_url = "http://overpass-api.de/api/interpreter"

def get_locations(establishment, amenity_type="fast_food"):
    """
    Fetches the locations of a specified establishment in the US using the Overpass API.

    Parameters:
    - establishment (str): The name of the establishment (e.g., "McDonald's", "Walmart").
    - amenity_type (str): The type of amenity or shop (e.g., "fast_food" for restaurants, "supermarket" for grocery stores).
    - - country_code (str): The ISO 3166-1 code of the country (e.g., "US" for United States, "DE" for Germany).
    The function saves the locations in a JSON file named after the establishment.
    """
    # Overpass QL query to get locations of the specified establishment in the US
    overpass_query = f"""
    [out:json];
    area["ISO3166-1"="US"]->.searchArea;
    node["{amenity_type}"]["name"="{establishment}"](area.searchArea);
    out body;
    """
    
    # Send the request to the Overpass API
    response = requests.post(overpass_url, data=overpass_query)
    data = response.json()

    # Extract the locations
    locations = [{"lat": element["lat"], "lng": element["lon"]} for element in data["elements"]]
    
    # Save to a JSON file
    filename = f"{establishment.lower().replace(' ', '_')}_locations_us.json"
    with open(filename, "w") as f:
        json.dump(locations, f)

    print(f"{establishment} locations in the US saved to {filename}")

# List of establishments to get locations for
establishments = [

]

# Fetch and save locations for each establishment
for est in establishments:
    get_locations(est["name"], est["amenity_type"])
"""
# Example of List of establishments to get locations for
establishments = [
    {"name": "McDonald's", "amenity_type": "fast_food"},  # Example of a fast food restaurant
    {"name": "Burger King", "amenity_type": "fast_food"}, # Another example of a fast food restaurant
    {"name": "KFC", "amenity_type": "fast_food"},         # Another example of a fast food restaurant
    {"name": "Walmart", "amenity_type": "supermarket"}    # Example of a supermarket
]


"""