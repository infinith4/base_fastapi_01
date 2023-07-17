from fastapi import FastAPI
from typing import Union
import requests
#import pprint
from utils.config import Config
app = FastAPI()

config = Config("config.yml").content

access_token = config["NFT_STORAGE_API"]["API_KEY"]
headers = {'Authorization': f'Bearer {access_token}'}

@app.get("/")
def read_root():
    baseurl = "https://api.nft.storage"
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