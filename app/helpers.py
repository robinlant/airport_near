from tabulate import tabulate
from app.airports_service import Airport

def format_airports_html(airports: list) -> str:
    headers = ["Name", "Größe", "Land", "IATA-Code", "Entfernung (km)"]
    airport_data = [
        [airport.name, airport.type, airport.country, airport.iata_code, f"{airport.distance:.2f}"] for airport in airports
    ]
    return tabulate(airport_data, headers=headers, tablefmt="html")

def prettify_airport_type(airport_type: str) -> str:
    switch = {
        "medium_airport": "Medium",
        "large_airport": "Groß",
    }
    
    return switch.get(airport_type, airport_type)

def prettify_airports_type(airports: list[Airport]) -> None:
    for i in airports:
        i.type = (prettify_airport_type(i.type))