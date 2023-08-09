import requests

data = {
    "id": "Coba-Coba lur",
    "title": "Produk Baru",
    "category": "Fresh",
    "price": "1,000,000",
    "description": "Description for the new shoe.",
    "colour": "Red",
    "url": "http://www.example.com/newshoe",
    "img_url": "http://www.example.com/newshoe.jpg"
}

response = requests.post("http://127.0.0.1:8000/nike/", json=data)

print(response.text)
