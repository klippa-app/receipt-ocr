# Receipt OCR for Receipt Processing & Information Extraction
This repository can be used to integrate Receipt OCR software to extract receipt information.
This receipt parser uses the DocHorizon OCR API to extract information.

### How Klippa Receipt OCR Works:

- Image Upload: You first need to upload the image of the receipt you want to process.
- Data Extraction: Klippa uses machine learning models and image processing techniques to analyze the image, identify key data points, and extract relevant information.
- Data Formatting: The extracted data is then formatted into a structured format (like JSON), which can easily be consumed by applications or compared with other datasets.
- Response: The service returns the structured data to your application, allowing you to process it as needed.

## Things you need
- A DocHorizon API key and/or license
- A receipt image
- A Python 3.6+ environment
- [_link to swagger docs_](https://dochorizon.klippa.com/api/swagger#/)

## How to Connect to Klippa Receipt OCR with Python
To use the Klippa Receipt OCR API in your Python script, you can follow these steps:

**Step 1: Set Up Your Environment** <br/>
You need to make sure you have Python installed on your system. You should also install the request library if it’s not already installed.
Also look for the requirements.txt file to see which things you need to install.

**Step 2: Obtain Credentials** <br/>
Sign up for Klippa’s services and get your API key. This key will be required to authenticate your requests.
>See how to get your API key in the section below; [here](#license--api-key)

**Step 3: Run Python Script** <br/>
In the repo is a sample Python script that demonstrates how to upload an image to Klippa and fetch the OCR results.


### Explanation:
- API_URL: Change this to the actual endpoint you need to use. Check [Klippa’s documentation](https://dochorizon.klippa.com/api/swagger#/) for the correct API URLs.
- API_KEY: Place your Klippa API key here.
- upload_receipt: This function uploads the image file to the Klippa OCR API and handles the response.
- files: The image file is opened in binary mode and sent as part of the request.
  Response Handling: The script checks if the request was successful and prints the extracted data or an error message.

### Important Notes:
Ensure you use secure methods to store and manage your API keys.
Always refer to the official Klippa API documentation for the most up-to-date information, including any changes in endpoints or request formats.
The API may have rate limits or require specific image formats—consult the documentation for these details.

>Please ensure that the image is the only object in the image with edges clearly visible.

<img src="/images/receipt-example-github.jpg" alt="receipt-example" width="400" height="400">

### Example
An example of a POST request using cURL:
Also, the following endpoint is used:
https://api.klippa.com/api/services/document_capturing/v1/components

<details>
<summary>Click here to see the full cURL command</summary>

```
curl -X POST \
  -H "Authorization: Bearer your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "components": {
      "barcode": {
        "barcode_types": ["code128"],
        "enabled": true
      },
      "fraud": {
        "enabled": true,
        "metadata": {
          "date": true,
          "editor": true
        },
        "visual": {
          "copy_move": true,
          "splicing": true
        }
      },
      "ocr": {
        "enabled": true
      }
    },
    "documents": [
      {
        "filename": "bonnetje.jpg",
        "data": "HIER_KOMT_DE_BASE64_DATA_VAN_JE_BESTAND"
      }
    ]
  }' \
  https://api.klippa.com/api/services/document_capturing/v1/components
```

</details>

<details>
<summary>The expected JSON schema with a 200 OK response</summary>

```
{
  "components": {
    "barcode": {
      "barcodes": [
        {
          "type": "string",
          "value": "string"
        }
      ],
      "candidates": [
        {
          "confidence": 0,
          "coordinates": [
            {
              "file": 0,
              "page": 0,
              "vertices": [
                [
                  0
                ]
              ]
            }
          ],
          "type": "string",
          "value": "string"
        }
      ]
    },
    "fraud": {
      "metadata": {
        "date": {
          "confidence": 0,
          "digitized": "string",
          "modified": "string",
          "original": "string"
        },
        "editor": {
          "confidence": 0,
          "found": [
            "string"
          ],
          "fraudulent": [
            "string"
          ]
        }
      },
      "summary": {
        "confidence": 0
      },
      "visual": {
        "copy_move": {
          "confidence": 0,
          "coordinates": [
            {
              "file": 0,
              "page": 0,
              "vertices": [
                [
                  0
                ]
              ]
            }
          ]
        },
        "splicing": {
          "confidence": 0,
          "coordinates": [
            {
              "file": 0,
              "page": 0,
              "vertices": [
                [
                  0
                ]
              ]
            }
          ]
        }
      }
    },
    "ocr": {
      "documents": [
        {
          "document_index": 0,
          "pages": [
            {
              "height": 0,
              "lines": [
                {
                  "coordinates": [
                    {
                      "file": 0,
                      "page": 0,
                      "vertices": [
                        [
                          0
                        ]
                      ]
                    }
                  ],
                  "text": "string",
                  "words": [
                    {
                      "coordinates": [
                        {
                          "file": 0,
                          "page": 0,
                          "vertices": [
                            [
                              0
                            ]
                          ]
                        }
                      ],
                      "text": "string"
                    }
                  ]
                }
              ],
              "page_index": 0,
              "text": "string",
              "width": 0
            }
          ]
        }
      ]
    }
  },
  "version": "string"
}
```

</details>

## License & API KEY
For this project and usage of the OCR technique, you would need to create an account and retrieve an API key.
Follow these steps to get your API key:
* Sign up via the [signup page](https://dochorizon.klippa.com/public/signup)
* Finish setting up the organization and create a first project
* Go to the project settings > Credentials page (1 & 2)
* Click on an existing credential or create a new one
* Make sure the right service is toggled on in the 'Access' tab (3 & 4)
* Go to the 'API Keys' tab and copy the API key
  * _Optional:_ Here you can also create a new API key if you want to have new keys for different use cases
* [Link to documentation](https://dochorizon.klippa.com/docs/platform/credentials) for further information

> Image of the Access page within an existing credential
<img src="/images/screenshot_credentials_access.png" alt="screenshot API key" width="1000" height="400">

> Image of the API Keys page within an existing credential
<img src="/images/screenshot_credentials_APIKEY.png" alt="screenshot API key" width="1000" height="400">

## Background & support
We at Klippa have 10 years of experience in OCR and have built a robust and scalable solution for many customers.
Receipt OCR is one of the most popular services. Since receipt information extraction is a complex task, we have developed a robust and scalable solution that can be used by anyone.
Thanks to the engine we use and receipt parser, you can extract information from receipts.
To learn more about the Receipt OCR software we use, visit this [page.](https://www.klippa.com/en/ocr/financial-documents/receipts/)

If you have any questions or need support, please [contact](mailto:dochorizon-support@klippa.com) us.
Or visit the general [website.](https://klippa.com/)

## Other supported languages
This repository contains a sample Python script that demonstrates how to upload an image to Klippa and fetch the OCR results.
But upon request we can also provide other languages. For example:
- cUrl
- NodeJS
- PHP
- GO
- C#/.NET
- Java