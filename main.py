import requests
import json
import os

# Defineer de basis-URL en het specifieke endpoint
BASE_URL = "https://dochorizon.klippa.com"
ENDPOINT = "/api/services/document_capturing/v1/components"

# Vervang de placeholder met jouw daadwerkelijke API-sleutel
# Bijvoorbeeld: "Bearer jouw_api_sleutel_hier"
API_KEY = "jouw_api_sleutel_hier"

# Controleer of de API_KEY is ingevuld
if API_KEY == "jouw_api_sleutel_hier":
    print("Fout: Vul je API-sleutel in de code in.")
    exit()

# Stel de headers in. Vaak is een Authorization header vereist.
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Combineer de URL's
url = f"{BASE_URL}{ENDPOINT}"

try:
    # Voer het GET-verzoek uit
    print(f"Bezig met aanroepen van: {url}")
    response = requests.get(url, headers=headers)

    # Verhoog een HTTPError voor slechte statuscodes (4xx of 5xx)
    response.raise_for_status()

    # Haal de JSON-data uit de response
    data = response.json()

    # Print de data in een leesbaar formaat
    print("Succesvol aangeroepen! Hier is de response:")
    print(json.dumps(data, indent=2))

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP-fout opgetreden: {http_err}")
    print(f"Response body: {response.text}")
except requests.exceptions.RequestException as req_err:
    print(f"Een verbindingsfout opgetreden: {req_err}")
except json.JSONDecodeError:
    print("Fout bij het decoderen van de JSON-response.")
    print(f"Onbewerkte response: {response.text}")