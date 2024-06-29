import requests  # type: ignore
import json

# Overpass API endpoint
overpass_url = "http://overpass-api.de/api/interpreter"

def get_locations(establishment, amenity_type=None, brand=None, country_code="US"):
    """
    Fetches the locations of a specified establishment in the specified country using the Overpass API.

    Parameters:
    - establishment (str): The name of the establishment (e.g., "McDonald's", "Walmart").
    - amenity_type (str, optional): The type of amenity or shop (e.g., "fast_food" for restaurants, "supermarket" for grocery stores).
    - brand (str, optional): The brand of the establishment (e.g., "McDonald's", "Walmart").
    - country_code (str): The ISO 3166-1 code of the country (e.g., "US" for United States, "DE" for Germany).
    The function saves the locations in a JSON file named after the establishment.
    """
    query_parts = []
    if amenity_type:
        query_parts.append(f'["amenity"="{amenity_type}"]')
    if establishment:
        query_parts.append(f'["name"="{establishment}"]')
    if brand:
        query_parts.append(f'["brand"="{brand}"]')
    
    query_filter = "".join(query_parts)
    
    # Overpass QL query to get locations of the specified establishment in the specified country
    overpass_query = f"""
    [out:json];
    area["ISO3166-1"="{country_code}"]->.searchArea;
    node{query_filter}(area.searchArea);
    out body;
    """
    
    # Send the request to the Overpass API
    response = requests.post(overpass_url, data=overpass_query)
    data = response.json()

    # Debugging: print the response data
    # print(json.dumps(data, indent=2))

    # Extract the locations
    locations = [{"lat": element["lat"], "lng": element["lon"]} for element in data.get("elements", [])]
    
    # Save to a JSON file
    filename = f"{establishment.lower().replace(' ', '_')}_locations_{country_code.lower()}.json"
    with open(filename, "w") as f:
        json.dump(locations, f)

    if locations:
        print(f"{establishment} locations in {country_code} saved to {filename}")
    else:
        print(f"No locations found for {establishment} in {country_code}")



# List of establishments to get locations for
establishments = [
     {"name": "McDonald's", "amenity_type": "fast_food", "brand": "McDonald's"},  # Example of a fast food restaurant
] 

"""

# Example of List of establishments to get locations for
establishments = [
    {"name": "McDonald's", "amenity_type": "fast_food", "brand": "McDonald's"},  # Example of a fast food restaurant
    {"name": "Burger King", "amenity_type": "fast_food", "brand": "Burger King"}, # Another example of a fast food restaurant
    {"name": "KFC", "amenity_type": "fast_food", "brand": "KFC"},         # Another example of a fast food restaurant
    {"name": "Walmart Supercenter", "amenity_type": "supermarket"}    # Example of a supermarket
]


"""


# Fetch and save locations for each establishment
for est in establishments:
    get_locations(est["name"], est.get("amenity_type"), est.get("brand"))

