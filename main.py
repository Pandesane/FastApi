from typing import Union

from fastapi import FastAPI
import uvicorn

from models.product import Product
from models.shop import Shop

from MetaData.metaData import shop, products, user

import routers.productsRouter as productsRouter

app = FastAPI()
app.include_router(productsRouter.router)

@app.get("/")
def root():
    return shop


@app.get("/getShop")
def getShop():
    return shop


@app.get("/getUser")
def getUser():
    return user

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port = 8000)