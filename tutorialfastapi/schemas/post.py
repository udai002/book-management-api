def postEntity(item)->dict:
    return {
        "id":item["_id"],
        "user_id":item['user_id'],
        "post":item["post"],
        "desc":item["desc"]
    }

def individual_books(books):
    return {
        "id":books['id'],
        "title":books['title'],
        "name":books['name'],
        "author":books['author']
    }

def all_books(books):
    return [individual_books(book) for book in books]