def postEntity(item)->dict:
    return {
        "id":item["_id"],
        "user_id":item['user_id'],
        "post":item["post"],
        "desc":item["desc"]
    }