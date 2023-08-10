import requests

BASE_URL = "http://127.0.0.1:8000/nike/"  # assuming your FastAPI server is running on default port

def delete_shoe(shoe_id):
    response = requests.delete(BASE_URL + shoe_id)
    
    if response.status_code == 200:
        print("Successfully deleted the shoe!")
        print(response.json())
    else:
        print(f"Failed to delete the shoe. Error: {response.text}")

if __name__ == "__main__":
    shoe_id_to_delete = input("Enter the ID of the shoe you want to delete: ")
    delete_shoe(shoe_id_to_delete)
