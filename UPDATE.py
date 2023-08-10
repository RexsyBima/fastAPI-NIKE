import requests
import json

BASE_URL = "http://127.0.0.1:8000/nike/"  # assuming your FastAPI server is running on default port

def update_shoe(shoe_id, updated_shoe_data):
    response = requests.put(BASE_URL + shoe_id, json=updated_shoe_data)
    
    if response.status_code == 200:
        print("Successfully updated the shoe!")
        print(response.json())
    else:
        print(f"Failed to update the shoe. Error: {response.text}")

if __name__ == "__main__":
    shoe_id_to_update = input("Enter the ID of the shoe you want to update: ")
    
    # Sample shoe data to update (you can take this dynamically as well)
    updated_data = {
        "id": shoe_id_to_update,
        "title": "Updated Title",
        "category": "Updated Category",
        "price": "Updated Price",
        "description": "Updated Description",
        "colour": "Updated Colour",
        "url": "Updated URL",
        "img_url": "Updated IMG URL"
    }
    
    update_shoe(shoe_id_to_update, updated_data)
