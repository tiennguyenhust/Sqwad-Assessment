from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

@app.get("/api/is_shopify_shop/")
async def is_shopify_shop(shop_url: str):
    r = requests.get(shop_url)
    return 'cdn.shopify.com' in r.text
         
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)