# Receipt OCR engine with an AI model
This repo is used for using our Receipt OCR engine to extract receipt information.
This receipt parser uses the DocHorizon OCR API to extract information.

### How Klippa Receipt OCR Works:

- Image Upload: You first need to upload the image of the receipt you want to process.
- Data Extraction: Klippa uses machine learning models and image processing techniques to analyze the image, identify key data points, and extract relevant information.
- Data Formatting: The extracted data is then formatted into a structured format (like JSON), which can easily be consumed by applications or compared with other datasets.
- Response: The service returns the structured data to your application, allowing you to process it as needed.

## Things you need
- A DocHorizon API key and/or license > read more, then click [here](#license)
- A receipt image
- A Python 3.6+ environment
- [_link to our swagger docs_](https://dochorizon.klippa.com/api/swagger#/)

## How to Connect to Klippa Receipt OCR with Python
To utilize the Klippa Receipt OCR API in your Python script, you can follow these steps:

**Step 1: Set Up Your Environment** <br/>
You need to make sure you have Python installed on your system. You should also install the request library if it’s not already installed.
Also look for our requirement file to see which things you need to install.

**Step 2: Obtain Credentials** <br/>
Sign up for Klippa’s services and get your API key. This key will be required to authenticate your requests.

**Step 3: Run Python Script** <br/>
In the repo is a sample Python script that demonstrates how to upload an image to Klippa and fetch the OCR results.


### Explanation:
- API_URL: Change this to the actual endpoint you need to use. Check Klippa’s documentation for the correct API URLs.
- API_KEY: Place your Klippa API key here.
- upload_receipt: This function uploads the image file to the Klippa OCR API and handles the response.
- files: The image file is opened in binary mode and sent as part of the request.
  Response Handling: The script checks if the request was successful and prints the extracted data or an error message.

### Important Notes:
Ensure you utilize secure methods to store and manage your API keys.
Always refer to the official Klippa API documentation for the most up-to-date information, including any changes in endpoints or request formats.
The API may have rate limits or require specific image formats—consult the documentation for these details.

>Please ensure that the image is the only object in the image. With edges clearly visible.

<img src="/images/receipt-example-github.jpg" alt="receipt-example" width="400" height="400">

## License
For this project and usage of our OCR technique you would need to create an account
on [our product page](https://dochorizon.klippa.com/)
* sign up
* finish setting up the organization and create a first project
* get your API key in the project settings > credentials section

## Background & support
We at Klippa have 10 years of experience in OCR and have built a robust and scalable solution for our customers.
If you have any questions or need support, please [contact](mailto:dochorizon-support@klippa.com) us.
Or visit our [website](https://klippa.com/)