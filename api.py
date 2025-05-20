
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks from JSON
with open("marks.json") as f:
    data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    marks = [entry["marks"] for entry in data if entry["name"] in name]
    return {"marks": marks}
