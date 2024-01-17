from fastapi import APIRouter,Body,UploadFile
from FileManager.fileManager import FileManager
from MetaData.metaData import products
from models.product import Product

router = APIRouter()


@router.get('/getProduct/{index}')
def getProduct(index: int = 0, last: bool = False):
    if last:
        return products[-1]
    if index < len(products):
        return products[index]
    else:
        return 'Product Not Found'


@router.get('/getProducts')
def getProducts(length: int = 10):
    for index in range(length):
        yield products[index]


@router.post('/addNewProduct')
def addNewProduct(product: Product):
    products.append(product)
    
    dir = FileManager(shopDir = 'Pande')
    return dir.path.exists()
    return product



def createDirectory(shopDirName: str):
    dir = FileManager(shopDir = shopDirName)
    return dir.path.exists()

@router.post('/uploadFile')
def uploadFile(file: UploadFile,shopDirName: str|None= 'Pande',):
   dir = FileManager(shopDir = shopDirName)
   dir.saveFile(file.filename, file.file)
        