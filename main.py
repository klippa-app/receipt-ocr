import requests

# Replace with your actual Klippa API endpoint and API key
API_URL = 'https://api.klippa.com/v1/receipt-ocr'  # This is a placeholder URL; please check the actual API documentation.
API_KEY = 'your_api_key_here'

def upload_receipt(image_path):
    # Define the headers for authentication
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    # Open the image file in binary mode
    with open(image_path, 'rb') as image_file:
        # Prepare the files to be sent in the request
        files = {
            'file': image_file,
        }
        # Make a POST request to the Klippa API
        response = requests.post(API_URL, headers=headers, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            return result
        else:
            # Handle errors, e.g., print the error message returned by Klippa
            print(f"Error: {response.status_code}, {response.text}")
            return None

# Example usage
if __name__ == '__main__':
    image_path = 'path_to_your_receipt_image.jpg'
    result = upload_receipt(image_path)
    if result:
        print("Extracted Data:", result)