import requests
import os

def generate_image(category):
    # Set up your Unsplash API access key
    ACCESS_KEY = '1xTBL3tn1biiThwGz-PjIFIwb-mXAeTppeNov8XB7mg'

    # Set up the API endpoint
    url = f'https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id={ACCESS_KEY}'

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the image URL from the response JSON
        data = response.json()
        image_url = data['urls']['regular']

        # Download the image
        image_data = requests.get(image_url).content
        with open('generated_image.jpg', 'wb') as f:
            f.write(image_data)
        
        print("Image generated successfully!")
    else:
        print("Failed to generate image. Status code:", response.status_code)

if __name__ == "__main__":
    category = input("Enter a category (e.g., 'nature', 'food', 'architecture'): ")
    generate_image(category)