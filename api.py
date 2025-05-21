from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks from JSON
with open("q-vercel-python.json") as f:
    data = json.load(f)

@app.get("/api")
def get_marks(name: List[str] = Query(default=[])):
    with open("q-vercel-python.json") as f:
        data = json.load(f)

    print("Incoming query names:", name)
    marks = [entry["marks"] for entry in data if entry["name"] in name]
    print("Matched marks:", marks)
    return {"marks": marks}
