from fastapi import FastAPI, HTTPException
import json, aiofiles
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
@app.get("/")
def welcome():
    return {"This is" : "NikeScrapedFASTAPI"}

@app.get("/nike/")
async def read_shoes():
    async with aiofiles.open('tes.json', mode='r', encoding='utf-8') as f:
        shoes = json.loads(await f.read())
    return shoes

# Read shoe by ID
@app.get("/nike/{shoe_id}")
async def read_shoe(shoe_id: str):
    async with aiofiles.open('tes.json', mode='r', encoding='utf-8') as f:
        shoes = json.loads(await f.read())
    for shoe in shoes:
        if shoe['id'] == shoe_id:
            return shoe
    raise HTTPException(status_code=404, detail="Shoe not found")


# Create a new shoe
@app.post("/nike/")
async def create_shoe(shoe: Shoe):
    async with aiofiles.open('tes.json', mode='r', encoding='utf-8') as f:
        shoes = json.loads(await f.read())

    shoes.append(shoe.dict())

    async with aiofiles.open('tes.json', mode='w', encoding='utf-8') as f:
        await f.write(json.dumps(shoes))
    
    return shoe
# Update a shoe
@app.put("/nike/{shoe_id}")
async def update_shoe(shoe_id: str, shoe: Shoe):
    async with aiofiles.open('tes.json', mode='r', encoding='utf-8') as f:
        shoes = json.loads(await f.read())

    for index, existing_shoe in enumerate(shoes):
        if existing_shoe['id'] == shoe_id:
            shoes[index] = shoe.dict()
            async with aiofiles.open('tes.json', mode='w', encoding='utf-8') as f:
                await f.write(json.dumps(shoes))
            return shoe
    
    raise HTTPException(status_code=404, detail="Shoe not found")

# Delete a shoe
@app.delete("/nike/{shoe_id}")
async def delete_shoe(shoe_id: str):
    async with aiofiles.open('tes.json', mode='r', encoding='utf-8') as f:
        shoes = json.loads(await f.read())

    for index, existing_shoe in enumerate(shoes):
        if existing_shoe['id'] == shoe_id:
            del shoes[index]
            async with aiofiles.open('tes.json', mode='w', encoding='utf-8') as f:
                await f.write(json.dumps(shoes))
            return {"status": "Shoe deleted"}

    raise HTTPException(status_code=404, detail="Shoe not found")