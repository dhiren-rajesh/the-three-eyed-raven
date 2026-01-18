import requests

BASE_URL= "https://ergast.com/api/f1"

def fetch_f1_api(endpoint: str) -> dict:
    """
    Fetch Formula 1 data from Ergast API

    The enpoint must be a valid Ergast path:
    - current/driverStandings
    - past/driverStandings
    - 2008/japan/results
    - drivers/verstappen
    """

    url = f"{BASE_URL}/{endpoint}.json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
