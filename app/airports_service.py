from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pandas as pd
import logging
import re

@dataclass
class Location:
    latitude: float
    longitude: float
    address: str

@dataclass
class Airport:
    name: str
    type: str
    country: str
    iata_code: str
    distance: float

class AirportsService:
    def __init__(self, airports_file_path: str):
        self._airports = pd.read_csv(airports_file_path)
        self.geolocator = Nominatim(user_agent="airport_locator")
    
    def _get_location_by_city(self, city_name: str) -> Location:
        if re.fullmatch(r"\d*", city_name):
            raise ValueError(f"{city_name} is not a valid city name!")
        location = self.geolocator.geocode(city_name)
        if not location:
            raise ValueError(f"City '{city_name}' not found!")
        return Location(
            latitude=location.latitude,
            longitude=location.longitude,
            address=location.address,
        )

    def _get_location_by_postal_code(self, postal_code: str) -> Location:
        search_query = f"{postal_code}, Deutschland"
        location = self.geolocator.geocode(search_query)
        if not location or not location.address.endswith(", Deutschland"):
            raise ValueError(f"Postal code '{postal_code}' not found!")
        return Location(
            latitude=location.latitude,
            longitude=location.longitude,
            address=location.address,
        )
        
    def _get_location_by_city_and_code(self, city_name: str, postal_code: str) -> Location:
        location = self.geolocator.geocode(f"{postal_code}, {city_name}")
        if not location:
            raise ValueError(f"City '{postal_code}, {city_name}' not found!")
        return Location(
            latitude=location.latitude,
            longitude=location.longitude,
            address=location.address,
        )
    
    def _find_nearest_airports(self, latitude: float, longitude: float, amount: int = 5) -> list[Airport]:
        if amount <= 0:
            raise ValueError("Amount of airports can't be less than 1.")
        distances = []
        for _, airport in self._airports.iterrows():
            airport_coords = (airport['latitude_deg'], airport['longitude_deg'])
            distance = geodesic((latitude, longitude), airport_coords).kilometers
            distances.append(
                Airport(
                    name=airport['name'],
                    type=airport['type'],
                    country=airport['iso_country'],
                    iata_code=airport.get('iata_code', ''),
                    distance=distance
                )
            )
        
        distances.sort(key=lambda x: x.distance, reverse=False)
        return distances[:amount]
    
    def search_by_city(self, city_name: str, amount: int = 5) -> tuple[list[Airport], Location]:
        location = self._get_location_by_city(city_name)
        return self._find_nearest_airports(location.latitude, location.longitude, amount), location
    
    def search_by_postal_code(self, postal_code: str, amount: int = 5) -> tuple[list[Airport], Location]:
        location = self._get_location_by_postal_code(postal_code)
        return self._find_nearest_airports(location.latitude, location.longitude, amount), location
    
    def search_by_city_and_code(self, city_name: str, postal_code: str, amount: int = 5) -> tuple[list[Airport], Location]:
        location = self._get_location_by_city_and_code(postal_code=postal_code, city_name=city_name)
        return self._find_nearest_airports(location.latitude, location.longitude, amount), location