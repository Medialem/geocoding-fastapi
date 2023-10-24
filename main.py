from typing import Optional
from fastapi import FastAPI
from utils import google_map_geocoding

app = FastAPI()




@app.get("/geocoding")
def geocoding(query: str, token: str):
    data = google_map_geocoding(query, token)
    print(f'>>>>>> {data}')
    return data