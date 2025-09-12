import base64
import requests

# Replace with your actual Klippa API endpoint and API key
API_URL = 'https://dochorizon.klippa.com/api/services/document_capturing/v1/components'
API_KEY = 'insert Klippa API key here'


def upload_receipt(image_path: str):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }

    with open(image_path, "rb") as handle:
        base64_file = base64.b64encode(handle.read()).decode("utf-8")

    request = {
        "documents": [
            {
                "data": base64_file,
            }
        ],
        "components": {
            "barcode": {
                "barcode_types": [
                    "string"
                ],
                "enabled": True
            },
            "fraud": {
                "enabled": True,
                "metadata": {
                    "date": True,
                    "editor": True
                },
                "visual": {
                    "copy_move": True,
                    "splicing": True
                }
            },
            "ocr": {
                "enabled": True
            }
        },
    }

    response = requests.post(
        url=API_URL,
        headers=headers,
        json=request,
        timeout=60
    )

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


# Example usage
if __name__ == '__main__':
    image_path = "Insert path where you receipt is stored on your PC"
    result = upload_receipt(image_path)
    if result:
        print("Extracted Data:", result)