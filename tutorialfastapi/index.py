from fastapi import FastAPI;
from routers.post import post;

app = FastAPI()
app.include_router(post)