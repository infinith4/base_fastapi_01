import uvicorn
from fastapi import FastAPI
from typing import Union
import requests
#import pprint
from utils.config import Config
app = FastAPI()

config = Config("config.yml").content

baseurl = config["NFT_STORAGE_API"]["BASE_URL"]

access_token = config["NFT_STORAGE_API"]["API_KEY"]
headers = {'Authorization': f'Bearer {access_token}'}

@app.get("/")
def read_root():
    res = requests.get(url=f"{baseurl}/", headers=headers)
    #pprint(res)
    print(res.content)

    return {"msg": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/items_list/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

@app.post("/upload")
async def update_image(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    did = ""
    headers['x-agent-did'] = f'{did}'
    print(headers)
    res = requests.post(url=f"{baseurl}/upload", headers=headers)
    #pprint(res)
    print(res.content)
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)