from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel

app = FastAPI()

class Shoe(BaseModel):
    id: str
    title: str
    category: str
    price: str
    description: str
    colour: str
    url: str
    img_url: str
# Read all shoes

@app.get("/nike/")
def read_shoes():
    with open('tes.json', 'r', encoding='utf-8') as f:
        shoes = json.load(f)
    return shoes

# Read shoe by ID
@app.get("/nike/{shoe_id}")
def read_shoe(shoe_id: str):
    with open('tes.json', 'r', encoding='utf-8') as f:
        shoes = json.load(f)
    for shoe in shoes:
        if shoe['id'] == shoe_id:
            return shoe
    raise HTTPException(status_code=404, detail="Shoe not found")

# Create a new shoe
@app.post("/nike/")
def create_shoe(shoe: Shoe):
    with open('tes.json', 'r', encoding='utf-8') as f:
        shoes = json.load(f)

    shoes.append(shoe.dict())
    
    with open('tes.json', 'w', encoding='utf-8') as f:
        json.dump(shoes, f)
    
    return shoe

# Update a shoe
@app.put("/nike/{shoe_id}")
def update_shoe(shoe_id: str, shoe: Shoe):
    with open('tes.json', 'r', encoding='utf-8') as f:
        shoes = json.load(f)

    for index, existing_shoe in enumerate(shoes):
        if existing_shoe['id'] == shoe_id:
            shoes[index] = shoe.dict()
            with open('tes.json', 'w', encoding='utf-8') as f:
                json.dump(shoes, f)
            return shoe
    
    raise HTTPException(status_code=404, detail="Shoe not found")

# Delete a shoe
@app.delete("/nike/{shoe_id}")
def delete_shoe(shoe_id: str):
    with open('tes.json', 'r', encoding='utf-8') as f:
        shoes = json.load(f)

    for index, existing_shoe in enumerate(shoes):
        if existing_shoe['id'] == shoe_id:
            del shoes[index]
            with open('tes.json', 'w', encoding='utf-8') as f:
                json.dump(shoes, f)
            return {"status": "Shoe deleted"}

    raise HTTPException(status_code=404, detail="Shoe not found")