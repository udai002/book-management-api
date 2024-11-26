from fastapi import FastAPI , Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# karumuriudaisai002
# d7PsKXVZ4lRw87EX
app = FastAPI()
app.mount('/static' , StaticFiles(directory='static') , name="static")
templates = Jinja2Templates(directory='templates')

conn = MongoClient("mongodb+srv://karumuriudaisai002:d7PsKXVZ4lRw87EX@cluster0.w6lat9a.mongodb.net/?authMechanism=DEFAULT")

@app.get("/" , response_class=HTMLResponse)
async def read_item(request:Request): 
    doc = conn.posts.posts.find({})
    user_name = ""
    for items in doc:
        user_name = items['user']
    return templates.TemplateResponse("index.html" ,{"request":request , "user":user_name})

@app.get("/page", response_class=HTMLResponse)
async def read_items(request: Request):
    return templates.TemplateResponse("page.html", {"request": request})

@app.get('/books')
async def getAllBook(request:Request):
        allBook =  conn.book.find({})
        return allBook

@app.post('/books')
async def addBooks(request:Request):
     addBook = conn.book.create_collection({})
     jsonObject = jsonable_encoder({"data":addBook})
     return JSONResponse(jsonObject)

@app.delete('/book/:id')
async def deleteBook(request:Request):
     deleteBook = conn.book.drop_collection({})
     JSONResponseObject = jsonable_encoder({"status":"true"})
     return JSONResponse(JSONResponseObject)

@app.get('/book/:id')
async def getOneBook(id):
     getABook = conn.book.get_collection({})
     jsonObject = jsonable_encoder({"status":"true" , "data":getABook})
     return jsonObject

