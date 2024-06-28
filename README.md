# Establishment Locations Fetcher

This script fetches locations of various establishments in the world using the Overpass API and saves them into JSON files.

## `get_locations` Function

Fetches the locations of a specified establishment using the Overpass API.

### Parameters

- `establishment (str)`: The name of the establishment (e.g., "McDonald's", "Walmart").
- `amenity_type (str)`: The type of amenity or shop (e.g., "fast_food" for restaurants, "supermarket" for grocery stores).
- `country_code (str)`: The ISO 3166-1 code of the country (e.g., "US" for United States, "DE" for Germany).

### Functionality

The function saves the locations in a JSON file named after the establishment.

## Example List of Establishments to Get Locations For

```python
establishments = [
    {"name": "McDonald's", "amenity_type": "fast_food"},  # Example of a fast food restaurant
    {"name": "Burger King", "amenity_type": "fast_food"}, # Another example of a fast food restaurant
    {"name": "KFC", "amenity_type": "fast_food"},         # Another example of a fast food restaurant
    {"name": "Walmart", "amenity_type": "supermarket"}    # Example of a supermarket
]
```
### Reference for Amenity Types
Amenity types can be found on the following OpenStreetMap Wiki:
https://wiki.openstreetmap.org/wiki/Template:Map_Features:amenity#:~:text=Amenity%20Used%20to%20map%20facilities%20used%20by%20visitors,toilets%2C%20telephones%2C%20banks%2C%20pharmacies%2C%20cafes%2C%20parking%20and%20schools

### Usage
Run pip install requests on the terminal
Run download_establishment_locations_us.py
The JSON should be downloaded to the same location as the downloader.
