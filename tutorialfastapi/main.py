from fastapi import FastAPI
from pymongo import MongoClient
from schemas.post import all_books , individual_books
from models.book import Books
# karumuriudaisai002
# d7PsKXVZ4lRw87EX
app = FastAPI()


conn = MongoClient("mongodb+srv://karumuriudaisai002:ky9KEuzCnFcOPaku@cluster0.k5uzy.mongodb.net/")
db = conn.books
collection = db['books']


@app.get('/books')
async def getAllBook():
        allBook =  collection.find({})
        return all_books(allBook)

@app.post('/books')
async def addBooks(new_books:Books):
    addBook = collection.insert_one(dict(new_books))     
    return individual_books(addBook)

@app.delete('/book/:id')
async def deleteBook(id):
     deleteBook = collection.drop_collection({id})
     

@app.get('/book/:id')
async def getOneBook(id):
     getABook = collection.get_collection({id})
     

