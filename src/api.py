import requests

BASE_URL= "https://ergast.com/api/f1"

def normalize_endpoint(endpoint: str) -> str:
    endpoint = endpoint.strip()
    if endpoint.startswith("http"):
        endpoint = endpoint.split("api/f1/")[-1]
    endpoint = endpoint.lstrip("/")
    if endpoint.endswith(".json"):
        endpoint = endpoint[:-5]

    return endpoint


def fetch_f1_api(endpoint: str) -> dict:
    """
    Fetch Formula 1 data from Ergast API

    The enpoint must be a valid Ergast path:
    - current/driverStandings
    - past/driverStandings
    - 2008/japan/results
    - drivers/verstappen
    """

    endpoint = normalize_endpoint(endpoint)
    url = f"{BASE_URL}/{endpoint}.json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
