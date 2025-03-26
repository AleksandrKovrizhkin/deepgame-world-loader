from fastapi import FastAPI
from pydantic import BaseModel
from parser import analyze_world

app = FastAPI()

class WorldText(BaseModel):
    world_text: str

@app.post("/load-world")
def load_world(data: WorldText):
    structured_world = analyze_world(data.world_text)
    return {
        "message": "Мир проанализирован",
        "structured_world": structured_world
    }
